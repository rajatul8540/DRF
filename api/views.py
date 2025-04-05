from django.shortcuts import render
from django.http import JsonResponse

def students_view(request):
    students = {
            "id": 1,
            "name": "John Doe",
            "age": 28
        }
    
    
    
    # Return the list of students in a structured format
    return JsonResponse(students)
