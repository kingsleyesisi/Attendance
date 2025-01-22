from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance

def index(request):
    # Views goes in here
    return render(request, 'index.html')

def save_attendance(request):
    if request.method == 'POST':
        name = request.POST['name']
        Matric_No = request.POST['Matric_No']
        contact = request.POST['contact']

        if Attendance.objects.filter(name=name).exists() or Attendance.objects.filter(Matric_No=Matric_No).exists():
            messages.error(request, 'Name or Matric Number already exists.')
            return redirect('duplicate')

        data = Attendance.objects.create(name=name, 
                                         Matric_No=Matric_No, 
                                         contact=contact)
        data.save()
    return redirect('/')

def view_attendance(request):
    attendance = Attendance.objects.all()
    data = {'Attendance': attendance}

    return render(request, 'view_attendance.html', data)


def duplicate(request):
    # The view for duplicate entery
    return render(request, 'duplicate.html')