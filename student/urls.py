from django.urls import path , include
from . import views

urlpatterns = [
    path('dashboard/',views.student_dashboard , name="student_dashboard"),
    path('attendance/',views.student_attendance , name="student_attendance"),
]