from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs=
                                                                    {'placeholder': 'Your Username',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs=
                                                                    {'placeholder': 'Your Password',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))
class SignupForm(UserCreationForm):
    #email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(required=True,widget=forms.TextInput(attrs=
                                                                    {'placeholder': 'Your Username',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs=
                                                                    {'placeholder': 'Your Email Address',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs=
                                                                    {'placeholder': 'Your Password',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs=
                                                                    {'placeholder': 'Repeat Password',
                                                                     'class': 'w-full py-4 px-6 rounded-xl'
                                                                     }))