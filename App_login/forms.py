from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from App_login.models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserSignUpForm(UserCreationForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='BD')
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'picture']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'picture']
