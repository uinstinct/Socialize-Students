from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    return render(request,'landingpage.html')


def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', {'students': students})

@login_required
def list_student(request, username):
    student =  get_object_or_404(Student, username=username)
    return render(request, 'students/profilepage.html', {'student':student})

def new_student(request):

	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():

			newStudent = form.save(commit=False)

			user = User.objects.create_user(newStudent.username, newStudent.email, newStudent.password)
			# print(user)
			user.save()

			newStudent.state='Jadiop'
			newStudent.save()
			return redirect('list_student', username=newStudent.username)

	else:
		form = StudentForm()
	return render(request,'students/new_student.html',{'form':form})

	def logout_view(request):
		logout(request)
		return redirect('/')