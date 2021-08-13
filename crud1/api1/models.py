from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
    
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

class Employee(models.Model):
    title = models.ForeignKey(Role, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    
    
    def __str__(self):
         return self.first_name ,self.last_name
     


     
     
