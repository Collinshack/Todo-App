from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('delete_task/<str:pk>', views.deleteTask, name='deleteTask'),
    path('edit_task/<str:pk>', views.editTask, name='editTask'),
    
]
