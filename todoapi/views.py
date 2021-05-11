from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

# Create your views here.

# def apiHomeView(request):
#     return JsonResponse('Welcome to the API home', safe=False)



#the home view with instructions on how to use the api
@api_view(['GET'])
def apiHomeView(request):
    api_urls = {
        'INFO': 'HOW TO USE THIS API',
        '-----------------': '---------------------------',
        'List all Task' : 'list-task/',
        'View details of one task': 'view-task/<int:pk>',
        'Create a new task': 'create-task/<int:pk>',
        'Update an existing task': 'update-task/<int:pk>',
        'Delete an existing task': 'delete-task/<int:pk>',
    }

    return Response(api_urls)

#view for listing all tasks
@api_view(['GET'])
def listTask(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


#view for reading the details of one task
@api_view(['GET'])
def viewTask(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


#view for creating a new task
@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



#view for updating a task
@api_view(['PUT'])
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#view for updating a task
@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()

    return Response("Item Deleted")