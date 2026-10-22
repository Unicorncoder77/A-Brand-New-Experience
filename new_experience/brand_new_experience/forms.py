from django import forms 
from django.core.validators import MinLengthValidator
from django.forms import ModelForm 
import datetime 
from .models import * 
from django.db import transaction 
from django.contrib.auth import get_user_model

User = get_user_model()

class reviewerRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=20, widget=forms.TextInput, required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    @transaction.atomic 
    def save(self):
        user = super().save(commit=False)
        user.is_reviewer = True
        regPass = self.cleaned_data.get('password')
        user.set_password(regPass)
        user.save()
        reviewer = Reviewer.objects.create(user=user)

        return user

class reviewerLoginForm(forms.Form):
     username = forms.CharField(label="Username", max_length=20, widget=forms.TextInput)
     password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password'}))

class bloggerRegisterForm(forms.ModelForm):
    fName = forms.CharField(label="First Name", max_length=99, widget=forms.TextInput)
    lName = forms.CharField(label="Last Name", max_length=99, widget=forms.TextInput)
    penname = forms.CharField(label="Pen Name", max_length=20, widget=forms.TextInput)
    email = forms.EmailField(label="Email", widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password'}))

    class Meta:
            model = User 
            fields = ['username', 'email', 'password']

    @transaction.atomic 
    def save(self):
        user = super().save(commit=False)
        user.is_blogger = True 
        regPass = self.cleaned_data.get('password')
        user.set_password(regPass)
        user.save()
        

        bloggerPen = self.cleaned_data.get('penname')
        bloggerFirst = self.cleaned_data.get('fName')
        bloggerLast = self.cleaned_data.get('lName')
        bloggerEmail = self.cleaned_data.get('email')
        blogger = Blogger.objects.create(user=user, username=bloggerPen, first_name=bloggerFirst, last_name=bloggerLast, email=bloggerEmail)

        return user
    