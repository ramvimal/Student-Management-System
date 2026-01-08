from django.shortcuts import render , redirect
from accounts.models import CustomUser
from teachers.models import Attendance
from django.contrib.auth.decorators import login_required
# Create your views here.

def student_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'student':
        return redirect("login")
    
    username = request.user
    student = CustomUser.objects.get(username=username)

    return render(request, 'student/student_dashbord.html', {'student': student})


def student_attendance(request):
    if request.user.is_authenticated:
        username = request.user.username
        student = CustomUser.objects.get(username=username)
        records = Attendance.objects.filter(student=student).order_by('-date')

        return render(request, 'student/view_attendance.html', {"student":student,'records': records})
    else:
        return redirect('login')