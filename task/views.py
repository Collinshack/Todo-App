from django.shortcuts import render, redirect
from .models import Taskdb
from .form import TaskForm

# Create your views here.

def mainPage(request):
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
    return redirect('mainPage')

def editTask(request, pk):
    todos = Taskdb.objects.get(id = pk)
    editForm = TaskForm(instance=todos)
    if request.method == 'POST':
        editForm = TaskForm(request.POST, instance = todos)
        if editForm.is_valid():
            editForm.save()
            return redirect('mainPage')
    return render(request, 'editingpage.html', {'todo':todos, 'editForm':editForm})