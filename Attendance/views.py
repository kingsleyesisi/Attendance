from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance

def index(request):
    # Home Page
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
    return redirect('/success')

def view_attendance(request):
    attendance = Attendance.objects.all()
    data = {'Attendance': attendance}

    return render(request, 'view_attendance.html', data)


def duplicate(request):
    # The view for duplicate entery
    return render(request, 'duplicate.html')

def success(request):
    # The view for successful entery
    return render(request, 'success.html')