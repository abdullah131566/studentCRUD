from django.db import models
from django.core import validators


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, validators=[
        validators.MinLengthValidator(limit_value=5)
    ])

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100, validators=[
        validators.MinLengthValidator(limit_value=2),
        validators.RegexValidator(regex=r'^[a-zA-Z\s]*$', message='Field should only contain alphabets and spaces')
    ])
    email = models.EmailField(max_length=150, unique=True)
    course = models.ForeignKey(to=Course, on_delete=models.SET_NULL, null=True)
    password = models.CharField(max_length=300, validators=[
        validators.MinLengthValidator(limit_value=8)
    ])
