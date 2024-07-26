# events/forms.py
from django import forms
from .models import Student, Payment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'f_name', 'l_name', 'email', 'phone', 'registration_number',
            'dob', 'gender', 'course', 'region', 'parent_status', 'profile_picture'
        ]
        widgets = {
            'gender': forms.Select(choices=Student.GENDER_CHOICES),
            'parent_status': forms.Select(choices=Student.PARENT_STATUS_CHOICES),
        }
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['f_name', 'l_name', 'email', 'phone', 'dob', 'gender', 'course', 'region', 'parent_status', 'profile_picture']
