from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import JobberUser

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'email','first_name', 'password1', 'password2']
        

class CreateEmpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email','first_name', 'last_name', 'password1', 'password2']


