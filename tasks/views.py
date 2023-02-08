from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html',{'form':UserCreationForm,"error":"El nombre de usuario ya está registrado"})
        return render(request, 'signup.html',{'form':UserCreationForm, "error":"Las contraseñas no coinciden"})


    return render(request, "tasks.html")

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{'form': AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{'form': AuthenticationForm, 'error':'El usuario o la contraseña son incorrectos'})
        else:
            login(request,user)
            return redirect('tasks')
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.autor = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'create_task.html',{'form':TaskForm,'error':"Por favor revisa los valores ingresados"})


def tasks(request):
    task = Task.objects.filter(autor=request.user)
    return render(request, "tasks.html", {"task": task})


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id,autor=request.user)
    if request.method == "POST":
        task.completada = True
        task.save()
        return redirect("tasks")

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id,autor=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")




def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)
        #print(form)
        return render(request, 'task_detail.html', {'task':task,'form': form})
    else:
        if request.method == 'POST':
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(request.POST,instance=task)
            form.save()
            return redirect("tasks")
            pass
