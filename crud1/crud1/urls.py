# from rest_framework import routers
# from api.views import EmployeeView
# from rest_framework.routers import DefaultRouter

# router =DefaultRouter()

# router.register('employee/',views.EmployeeView)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api1.views import EmployeeView,RoleView

router = routers.DefaultRouter()
router.register('employee', EmployeeView)
router.register('role', RoleView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   
]
