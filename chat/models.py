from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class UserManagement(models.Model):
    name=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    department=models.CharField(max_length=200)

class Groups(models.Model):
    group_name=models.CharField(max_length=200)
    users=models.CharField(max_length=200)
    computers=models.CharField(max_length=200)

class Broadcast(models.Model):
    title=models.CharField(max_length=200)
    users=models.CharField(max_length=200)
    computers=models.CharField(max_length=200)

class Setting(models.Model):
    name=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    department=models.CharField(max_length=200)