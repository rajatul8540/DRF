from django.shortcuts import render
from django.http import JsonResponse
from students.models import Stduents
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.decorators import api_view # type: ignore\
from rest_framework.views import APIView
from employees.models import Employee

@api_view(['GET','POST'])
def students_view(request):
    if request.method == 'GET':
        students = Stduents.objects.order_by('-id').all()
        serialzer = StudentSerializer(students,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
    elif request.method =='POST':
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def student_detail_view(request,pk):
    try:
        student = Stduents.objects.get(pk=pk)
    except Stduents.DoesNotExist:
        return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =="PUT":
        serializer = StudentSerializer(student,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)  
        else:
            return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)
    elif request.method =="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

        
        
        
    
    

            
        
        
        

