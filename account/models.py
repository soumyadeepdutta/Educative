from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    choices = [
        ('Graduate', 'Graduate'),
        ('Masters', 'Masters'),
        ('Doctorate', 'Doctorate')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(choices=choices, max_length=10, default=choices[0][0])
