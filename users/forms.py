from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']

    # username = forms.CharField(label = 'Имя пользователя', widget=forms.TextInput(attrs={"autofocus": True,
    #                                                           "class": "form-control",
    #                                                             "placeholder": "Введите имя пользователя",
    #                                                             }))
    # password = forms.CharField(label = 'Пароль пользователя', widget=forms.PasswordInput(attrs={
    #     "autocomplete": "current-password",
    #     "class": "form-control",
    #     "placeholder": "Введите пароль",
    # }))

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('freelancer', 'Freelancer'),
    ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "phone_number", "password1", "password2", "user_type")



class ProfileForm(UserChangeForm):
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('freelancer', 'Freelancer'),
    ]
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'email', "user_type", 'position')
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    position = forms.CharField()
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)