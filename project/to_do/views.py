from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm, LoginForm, CreateTask
from django.contrib.auth import authenticate, login, logout
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


def Register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse ("please enter the valid details")
    else:
        form = RegisterForm()
        return render(request, 'to_do/register.html', {'form':form})


def Login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("user is not Find!!")
    else:
        form = LoginForm()
        return render(request, 'to_do/login.html', {'form':form})

@login_required
def Home_view(request):
    task = Task.objects.filter(created_by=request.user)
    return render (request, 'to_do/home.html', {'task':task})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save()
            task.created_by=request.user
            task.save()
            return redirect('home')
        else:
            return HttpResponse("enter valid details!")
    else:
        form = CreateTask()
        return render(request, 'to_do/create_task.html', {'form':form})
    

@login_required
def update_task(request, id):
    task = Task.objects.get(pk=id)
    if task.created_by != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("enter valid details!")
    else:
        form = CreateTask()
        return render(request, 'to_do/update.html', {'form':form})


@login_required
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    if task.created_by!=request.user:
        return redirect('to_do/home')
    else:
        task.delete()
        return redirect('home')


def Logout_view(request):
    logout(request)
    return redirect('login')