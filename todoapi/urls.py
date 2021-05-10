from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiHomeView , name = 'api_home'),
    path('list-task/', views.listTask, name = 'list-task'),
    path('view-task/<int:pk>', views.viewTask, name = 'view-task'),
    path('create-task/', views.createTask, name = 'create-task'),
    path('update-task/<int:pk>', views.updateTask, name = 'update-task'),
    path('delete-task/<int:pk>', views.deleteTask, name = 'delete-task'),
]
