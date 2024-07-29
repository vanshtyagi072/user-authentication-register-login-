# register api model

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser, Group, Permission
class Register(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True,default='example@example.com')
    password = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.user_name
    
class login(models.Model):
    email = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)
     
class employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_id  =  models.CharField(max_length=50, unique=True)    
    

