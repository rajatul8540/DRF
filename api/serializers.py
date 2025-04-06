from rest_framework import serializers  # type: ignore
from students.models import Stduents  # Typo fixed in model name
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):  # Capital "M" in ModelSerializer
    class Meta:
        model = Stduents
        fields = "__all__"  # Typo fixed: 'field' → 'fields'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


