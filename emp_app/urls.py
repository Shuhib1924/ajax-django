from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp, name='emp'),
    path('office', views.officeCRUD, name='office'),
    path('employee', views.employeeCRUD, name='employee'),
]

