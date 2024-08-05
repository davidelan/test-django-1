from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm, CustomUserCreationForm

# Landing page
def home(request):
    return render(request, 'home.html')

# User registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# User logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# List all TodoLists for the authenticated user
@login_required
def todo_lists(request):
    lists = TodoList.objects.filter(user=request.user)
    return render(request, 'todo_lists.html', {'lists': lists})

# View details of a specific TodoList
@login_required
def todo_list_detail(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk, user=request.user)
    return render(request, 'todo_list_detail.html', {'todo_list': todo_list})

# Add a new TodoList
@login_required
def add_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'add_todo_list.html', {'form': form})

# Edit an existing TodoList
@login_required
def edit_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', pk=todo_list.pk)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'edit_todo_list.html', {'form': form})

# Delete a TodoList
@login_required
def delete_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk, user=request.user)
    if request.method == 'POST':
        todo_list.delete()
        return redirect('todo_lists')
    return render(request, 'delete_todo_list.html', {'todo_list': todo_list})

# Add a new TodoItem to a specific TodoList
@login_required
def add_todo_item(request, list_pk):
    todo_list = get_object_or_404(TodoList, pk=list_pk, user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.todo_list = todo_list
            todo_item.save()
            return redirect('todo_list_detail', pk=todo_list.pk)
    else:
        form = TodoItemForm()
    return render(request, 'add_todo_item.html', {'form': form, 'todo_list': todo_list})

# Edit an existing TodoItem
@login_required
def edit_todo_item(request, list_pk, item_pk):
    todo_item = get_object_or_404(TodoItem, pk=item_pk, todo_list__pk=list_pk, todo_list__user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', pk=list_pk)
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'edit_todo_item.html', {'form': form, 'todo_list': todo_item.todo_list})

# Delete a TodoItem
@login_required
def delete_todo_item(request, list_pk, item_pk):
    todo_item = get_object_or_404(TodoItem, pk=item_pk, todo_list__pk=list_pk, todo_list__user=request.user)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list_detail', pk=list_pk)
    return render(request, 'delete_todo_item.html', {'todo_item': todo_item})
