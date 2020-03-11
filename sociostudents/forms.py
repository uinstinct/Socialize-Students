from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('username','name','year','college','interests','skills','city', 'state','bio',)