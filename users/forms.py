from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    account_type = forms.ChoiceField(choices=((1, ("Author")), (2, ("Non-Author"))))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'account_type']


