
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    rollno = models.IntegerField(blank=True, null=True)
    stream = models.CharField(max_length=30, default='Not selected')
    

    def __str__(self):
        return self.username
