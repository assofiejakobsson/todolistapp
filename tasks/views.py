from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import SharedList, TaskList, Task
from .forms import TaskForm, TaskListForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('task_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

#här
def create_task_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskListForm()
    return render(request, 'create_task_list.html', {'form': form})



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    shared_lists = SharedList.objects.filter(shared_with=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'shared_lists': shared_lists})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Create your views here.
def task_detail(request, task_list_id, task_id):
    task_list = get_object_or_404(TaskList, pk=task_list_id)
    task = get_object_or_404(Task, pk=task_id, task_list=task_list)
    return render(request, 'task_detail.html', {'task_list': task_list, 'task': task})