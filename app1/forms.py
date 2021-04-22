from django import forms
from .models import mymodel

# for user registration and login

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class web(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = '__all__'


# login
class logon(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class user_login_form(forms.Form):
    user_name= forms.CharField(max_length=50)
    psswd = forms.CharField(max_length=200,widget=forms.PasswordInput)