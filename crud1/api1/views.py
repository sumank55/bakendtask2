from django.shortcuts import render
from .serializers import EmployeeSerializers,RoleSerializer
from rest_framework import viewsets
from .models import Employee,Role
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','first_name','last_name','email']
    
    
    
class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer    
   

