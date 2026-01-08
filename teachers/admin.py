from django.contrib import admin
from .models import Attendance
# Register your models here.

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = ('student' , 'date' , 'status')
    fields = ('student' , 'date' , 'status') 
    list_filter = (['student' , 'date' , 'status'])
    search_fields = ('student__username', 'student__email', 'date')

