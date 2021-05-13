from django.urls import path
from .views import login_view, createAccount, logout_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', createAccount, name='register'),
]


