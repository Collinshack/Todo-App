
from logging import PlaceHolder
from django import forms 
from .models import Taskdb

class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={
        'id': 'taskField', 'placeholder': 'Enter a task' 
        }))
    class Meta:
        model = Taskdb
        fields = ['task',]
        