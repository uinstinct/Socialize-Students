from django import forms
from django.contrib.auth import get_user_model

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('username','password','email','name','year','college','interests','skills','city', 'state','bio',)