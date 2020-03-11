from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    username=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=100,default="shuriken")
    email=models.CharField(max_length=200,default="gren@ninja.com")
    name=models.TextField()
    year=models.IntegerField()
    college=models.TextField()
    interests=models.TextField()
    skills=models.TextField()
    city=models.TextField()
    state=models.TextField()
    bio=models.TextField(default="I am loving SocioStudent")
    def __str__(self):
        return self.username