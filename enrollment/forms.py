from django import forms
from .models import Student


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Student\'s Name',
            'email': 'Student\'s Email',
            'course': 'Register for course',
            'password': 'Password',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
            'password': forms.PasswordInput(render_value=True, attrs={
                'class': 'form-control'
            })
        }
        error_messages = {
            'password': {
                'min_length': 'Password must be %(limit_value)s characters long.'
            }
        }
