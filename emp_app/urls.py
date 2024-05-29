from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp, name='emp'),
]

