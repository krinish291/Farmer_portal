from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expert
from blog.models import  Query_Answer
from django.forms import ModelForm


class ExpertRegisterForm(ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    #File = forms.FileField()

    class Meta:
        model = Expert
        fields = ['username', 'password','Dp','category', 'email','File_Verify','description']

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Query_Answer
        fields = ['Query_Reply']