from django.shortcuts import redirect, render
from .models import Student
from django.contrib import messages
import os
# Create your views here.
def index(request):
    students = Student.objects.all()
    messages.info(request, 'Welcome to the Student App')
    return render(request, 'index.html', {'students': students})

def add(request):
    return render(request, 'add.html')

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})

def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        if len(request.FILES) != 0:
            imagen = request.FILES['imagen']
        else:
            imagen = 'uploads/sin-foto.png'
        Student.objects.create(first_name=first_name, last_name=last_name, email=email, age=age, imagen=imagen)
        messages.success(request, 'Student created successfully')
        return redirect('/')
    else:
        return redirect('/')

def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        link = request.POST['imagenInput']
        
        student = Student.objects.get(id=id)
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.age = age

        if len(request.FILES) != 0:
            if link != 'uploads/sin-foto.png':
                os.remove(student.imagen.path)
                imagen = request.FILES['imagen']
                student.imagen = imagen
            else:
                imagen = request.FILES['imagen']
                student.imagen = imagen
        else:
            student.imagen = link
        student.save()
        messages.success(request, 'Student updated successfully')
        return redirect('/')
    else:
        return redirect('/')

def delete(request, id):
    student = Student.objects.get(id=id)
    if student.imagen != 'uploads/sin-foto.png':
        os.remove(student.imagen.path)
    student.delete()
    messages.warning(request, 'Student deleted successfully')
    return redirect('/')
    