from django import forms
from .models import TodoList, TodoItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['text', 'completed']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
