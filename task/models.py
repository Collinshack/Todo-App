from django.db import models

# Create your models here.
class Taskdb(models.Model):
    task = models.CharField(max_length=50)
       
def __str__(self):
    return self.task


class UsersRegister(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password2= models.CharField(max_length=50)
