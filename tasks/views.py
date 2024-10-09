from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  # Import messages framework
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')  # Set success message
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        if 'completed' in request.POST:  # Check if the completed checkbox was submitted
            task.delete()  # Delete the task if it's marked as completed
            messages.success(request, 'Task was Completed!')  # Set success message
            return redirect('/')  # Redirect to the main page
        else:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()  # Update the task
                messages.success(request, 'Task updated successfully!')  # Set success message
                return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Task deleted successfully!')  # Set success message
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()  # Delete the task when it's marked as complete
    messages.success(request, 'Task completed successfully!')  # Set success message
    return redirect('/')
