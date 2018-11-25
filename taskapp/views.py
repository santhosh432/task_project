from django.shortcuts import render, redirect
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