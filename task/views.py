from django.shortcuts import render, redirect
from task.models import TaskModel
from . import forms
from . import models

def show(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show-tasks.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('task.show')
    else:
        task_form = forms.TaskForm()

    return render(request, 'add-task.html', {'form': task_form})

def edit(request, id):
    task = models.TaskModel.objects.get(id=id)
    task_form = forms.TaskForm(instance=task)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task.show')
        
    return render(request, 'edit-task.html', {'form': task_form})

def delete(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('task.show')
