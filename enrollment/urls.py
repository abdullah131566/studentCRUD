from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment, name='enrollment'),
    path('<int:student_id>/', views.enrollment_detail, name='enrollment_detail'),
    path('delete/<int:student_id>/', views.enrollment_delete, name='enrollment_delete')
]
