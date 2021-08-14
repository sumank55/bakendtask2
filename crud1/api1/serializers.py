from rest_framework import serializers
from .models import  Employee,Role


class EmployeeSerializers(serializers.ModelSerializer):
    title_name=serializers.CharField(source='title.name',read_only=True)
    class Meta:
        model=Employee
        fields=['id','title_name','first_name','last_name','email']
        
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)
        
    