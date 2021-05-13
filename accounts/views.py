from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def createAccount(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.info(request, 
                    "Something is Wrong: \n\n email must be in this format 'xyz@email.com' \n password must be 8 ot more digits, Contain Cap Letter and a Number"
                    )

        context = {'form': form}
        return render(request, 'register.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrect ')

        context = {}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')