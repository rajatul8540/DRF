from django.shortcuts import render
from django.http import JsonResponse
from students.models import Stduents
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.decorators import api_view # type: ignore\
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404

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
        employees = Employee.objects.order_by('-id').all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serialzer = EmployeeSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.error,status=status.HTTP_400_BAD_REQUEST)
   
   
class EmployeeDetails(APIView):
    def get_object(self,pk):
        try:
            return  Employee.objects.get(pk=pk)
        except  Employee.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer =EmployeeSerializer(employee)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def put(self,request,pk):
        empolyee = self.get_object(pk)
        serializer = EmployeeSerializer(empolyee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
        
        
        
        
        
        
        
        
        
    

        
        
        
    
    

            
        
        
        

