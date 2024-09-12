from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('task_list')  # Redirect to a success page or task list
    else:
        form = SignUpForm()
    
    return render(request, 'task/signup.html', {'form': form})


@login_required

@login_required
def task_list(request):
    # Default sorting field and direction
    default_sort_field = 'title'
    default_sort_dir = 'asc'
    
    # Get the sort field, direction, and filter from the query parameters
    sort_by = request.GET.get('sort', default_sort_field)
    sort_dir = request.GET.get('sort_dir', default_sort_dir)
    filter_by = request.GET.get('filter', None)

    # Define valid sort fields and directions to prevent invalid sorting
    valid_sort_fields = ['title', 'due_date', 'completed']
    valid_sort_dirs = ['asc', 'desc']

    # Sanitize sort_by and sort_dir parameters
    if sort_by not in valid_sort_fields:
        sort_by = default_sort_field
    if sort_dir not in valid_sort_dirs:
        sort_dir = default_sort_dir

    # Determine the sorting order
    sort_order = '' if sort_dir == 'asc' else '-'

    # Filter tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user)

    # Apply filter based on 'filter' query parameter
    if filter_by == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_by == 'uncompleted':
        tasks = tasks.filter(completed=False)

    # Apply sorting
    tasks = tasks.order_by(f"{sort_order}{sort_by}")

    # Pass the tasks and current filter, sort field, and direction to the template
    context = {
        'tasks': tasks,
        'current_sort': sort_by,
        'current_sort_dir': sort_dir,
        'filter': filter_by
    }
    return render(request, 'task/task_list.html', context)

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
    return render(request, 'task/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
