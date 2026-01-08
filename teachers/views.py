import re
from django.shortcuts import render , redirect
from accounts.models import CustomUser
from .models import Attendance
from results.models import Result

# Create your views here.

def teacher_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'teacher':
        return redirect('login')
    
    teacher = request.user

    return render(request, 'teacher/teacher_dashbord.html', {'teacher': teacher})

def take_attendance(request):
    # ✅ Ensure only teacher can access
    if not request.user.is_authenticated or request.user.role != 'teacher':
        return redirect('login')

    # ✅ Get all students only
    students = CustomUser.objects.filter(role='student')

    if request.method == 'POST':
        selected_date = request.POST.get('date')

        # ✅ Check if attendance already exists
        if Attendance.objects.filter(date=selected_date).exists():
            return render(
                request,
                'teacher/take_attendance.html',
                {'students': students, 'attendance_already': f"❌ Attendance for {selected_date} already added. ❌"}
            )

        # ✅ Save attendance for all students
        for student in students:
            status = request.POST.get(f"status_{student.id}")
            Attendance.objects.create(
                student=student,
                date=selected_date,
                status=status,
            )

        return render(
            request,
            'teacher/take_attendance.html',
            {'students': students, 'attendance_taken': f"✅ Attendance for {selected_date} added successfully. ✅"}
        )

    return render(request, 'teacher/take_attendance.html', {'students': students})

def make_result(request):
    if not request.user.is_authenticated or request.user.role != "teacher":
        return redirect("login")

    students = CustomUser.objects.filter(role="student")
    if request.method == "POST":
        student_username = request.POST.get('students')
        sem = request.POST.get('semester')
        try:
            student_obj = CustomUser.objects.get(username=student_username)
        except CustomUser.DoesNotExist:
            return render(request,"teacher/make_result.html",{'students':students,'student_not_found' : f"❌Student with username {student_username} not found.❌"})
        
        if Result.objects.filter(student=student_obj,sem=sem).exists():
            return render(request,"teacher/make_result.html",{'students':students,'marks_already_submit' : f"❌Marks of {student_username} for semester {sem} already exists.❌"})

        Result.objects.create(
            student=student_obj,
            sem = sem,
            seo = request.POST.get('seo'),
            c_sharp = request.POST.get('c'),
            php = request.POST.get('php'),
            python = request.POST.get('python'),
            java = request.POST.get('java'),
            ac_year = "2025-2026",
        )
        return render(request,"teacher/make_result.html",{'students':students,'mark_submit': f"✅Marks of {student_username} for semester {sem} added successfully.✅"})


            
    return render(request,"teacher/make_result.html",{'students':students})