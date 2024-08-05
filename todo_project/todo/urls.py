from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todo_lists/', views.todo_lists, name='todo_lists'),
    path('todo_lists/add/', views.add_todo_list, name='add_todo_list'),
    path('todo_lists/<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo_lists/<int:pk>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todo_lists/<int:pk>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todo_lists/<int:list_pk>/items/add/', views.add_todo_item, name='add_todo_item'),
    path('todo_lists/<int:list_pk>/items/<int:item_pk>/edit/', views.edit_todo_item, name='edit_todo_item'),
    path('todo_lists/<int:list_pk>/items/<int:item_pk>/delete/', views.delete_todo_item, name='delete_todo_item'),
]
