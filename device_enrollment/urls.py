
from django.urls import path
from device_enrollment import views

urlpatterns = [
    path('', views.home,name='home'),
    path('device_enrollment/add_device/', views.add_device,name='add_device')
]