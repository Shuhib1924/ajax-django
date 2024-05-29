from django.shortcuts import render
from .models import Employee, Office, OfficeForm, EmployeeForm
def emp(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        'officeForm' : OfficeForm,
        'employeeForm' : EmployeeForm
    }
    return render(request, 'emp.html', context)