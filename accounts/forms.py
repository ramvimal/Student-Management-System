from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    rollno = forms.CharField(max_length=20, required=False, label="Roll Number")
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'   # automatically set role
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
