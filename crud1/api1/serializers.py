from rest_framework import serializers
from .models import  Employee,Role


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['title','first_name','last_name','email']
        
        
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']
        
    