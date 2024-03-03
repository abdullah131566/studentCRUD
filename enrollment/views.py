from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from .forms import NewStudentForm


def enrollment(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewStudentForm()
    else:
        form = NewStudentForm()
    return render(request, 'enrollment/enrollment.html', {
        'form': form,
        'students': students
    })


def enrollment_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student_form = NewStudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
    else:
        student_form = NewStudentForm(instance=student)
    return render(request, 'enrollment/student_detail.html', {
        'student_form': student_form,
        'student_id': student_id
    })


def enrollment_delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    if student:
        student.delete()
        return HttpResponseRedirect('/enrollment/')
