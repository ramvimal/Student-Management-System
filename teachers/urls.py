from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.teacher_dashboard, name="teacher_dashboard"),
    path('attendance/',views.take_attendance, name="take_attendance"),
    path('make_result/',views.make_result, name="make_result"),
]
