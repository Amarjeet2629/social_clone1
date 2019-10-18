from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')


class UserProfileInfoForm(forms.ModelForm):
    #confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic', )

