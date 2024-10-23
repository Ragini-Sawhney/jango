from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    discription = models.CharField(max_length=1000)

# class Login(models.Model):
#     user_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)  
#     email = models.CharField(max_length=100)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
