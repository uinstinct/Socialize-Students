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

@login_required
def edit_student(request, username):
	# print(username)
	student = get_object_or_404(Student, username=username)

	# print(student.name)
	user = get_object_or_404(User, username=username)
	if request.method == "POST":
		print('here1')
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			editStudent=form.save(commit=False)

			print("printing user details below")
			print(editStudent)

			# changing the user account
			user.username=editStudent.username
			user.password=editStudent.password
			user.email=editStudent.email
			user.save();
			# changing the student account
			editStudent.city='Xaden'
			editStudent.save()
			return redirect('list_student', username=editStudent.username)
		else:
			print(form.errors)
	else:
		form=StudentForm(instance=student)
	return render(request, 'students/editProfile.html',{'student':student})

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
			if request.user.is_authenticated():
				logout(request)
				return render(request, 'registration/login.html')
			else:
				return render(request, 'students/profilepage.html', {'student':student})

	else:
		form = StudentForm()
	return render(request,'students/new_student.html',{'form':form})

def delete_student(request, username):
	student= get_object_or_404(Student, username=username)
	user= get_object_or_404(User, username=username)

	student.delete()
	user.delete()

	return redirect('/')

def logout_view(request):
	logout(request)
	return redirect('/')
