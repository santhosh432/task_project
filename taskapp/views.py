from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

def home(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    task = Task.objects.all()
    return render(request, 'home.html', context={'task':task, 'form':form})

def task_edit(request, pk):

    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')


    return render(request, 'edit.html', {'form': form})