from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import Task


def submit(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                redirect('/index')
            except:
                pass
        else:
            form = TaskForm()
        return render(request, 'app/app_index.html', {'form':form})

def index(request):
    tasks = Task.objects.all()
    return render(request, 'app/app_index.html', {'tasks':tasks})

def edit(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'app/app_display.html', {'task':task})

def display(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'app/app_index.html', {'task':task})

def update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST, instance = task)
    if form.is_valid():
        form.save()
        return redirect(index)
    return render(request, 'app/app_display.html', {'task': task})

def delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect(index)

"""
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

"""
