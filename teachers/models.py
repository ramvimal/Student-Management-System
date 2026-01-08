from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Present', 'Absent'
    
    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.date}"