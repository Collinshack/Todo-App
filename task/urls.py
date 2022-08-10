from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
     path('logout', views.logout, name='logout'),
    path('todoapp', views.todoapp, name='todoapp'),
    path('delete_task/<str:pk>', views.deleteTask, name='deleteTask'),
    path('edit_task/<str:pk>', views.editTask, name='editTask'),
    
]
