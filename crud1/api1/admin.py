from django.contrib import admin
from .models import Employee,Role


# Register your models here.
admin.site.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display='__all__'
    search_fields=('email')
    
    
admin.site.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


    
    