from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('students/', views.all_students, name='students'),
    path('students/<str:username>/', views.list_student,name='list_student'),
    path('students/new/',views.new_student,name='new_student'),
    path('students/<str:username>/edit/', views.edit_student, name='edit_student'),
    # we have a / at the end because otherwise path will matched against /<str:username>
]
