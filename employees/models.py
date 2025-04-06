from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=20, null=True, blank=True, default=None)
    emp_name = models.CharField(max_length=20, null=True, blank=True, default=None)
    designation = models.CharField(max_length=40, null=True, blank=True, default=None)

    def __str__(self):
        return self.emp_name

        
    
    
