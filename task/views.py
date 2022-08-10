from django.shortcuts import render, redirect
from .models import Taskdb
from .form import TaskForm
from django.contrib.auth.models import User, auth
from django.contrib import messages 
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('todoapp')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('/')
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                success_msg = messages.success(request, 'Account Successfully Created!')
                return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def todoapp(request):
    tasks = Taskdb.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'todoapp.html', {'form': form, 'tasks': tasks})


def deleteTask(request, pk):
    task = Taskdb.objects.get(id= pk)
    task.delete()
    return redirect('todoapp')

def editTask(request, pk):
    todos = Taskdb.objects.get(id = pk)
    editForm = TaskForm(instance=todos)
    if request.method == 'POST':
        editForm = TaskForm(request.POST, instance = todos)
        if editForm.is_valid():
            editForm.save()
            return redirect('todoapp')
    return render(request, 'editingpage.html', {'todo':todos, 'editForm':editForm})