from django.urls import path
from . import views


urlpatterns =[
    path('students/',views.students_view),
    path('student/<int:pk>/', views.student_detail_view),
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetails.as_view())
]