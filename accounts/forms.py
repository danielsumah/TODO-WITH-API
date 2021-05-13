from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    password1        = forms.CharField(
                        widget=forms.PasswordInput(
                            attrs={
                                'class': 'form-control',
                                'placeholder':'password',
                                'id': 'password1'
                                }
                            )
                        )
    password2        = forms.CharField(
                        widget=forms.PasswordInput(
                            attrs={
                                'class': 'form-control',
                                'placeholder':'confirm password',
                                'id': 'password2'
                                }
                            )
                        )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username':     forms.TextInput(attrs={'placeholder':"  username", 'id':'username'}),
            'email':        forms.TextInput(attrs={'placeholder':"  email", 'id':'email'}),
        }

        
        