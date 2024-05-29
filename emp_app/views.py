from django.shortcuts import render
from .models import Employee, Office, OfficeForm, EmployeeForm
from django.http import JsonResponse
def emp(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        'officeForm' : OfficeForm,
        'employeeForm' : EmployeeForm
    }
    return render(request, 'emp.html', context)

def officeCRUD(request):
    if request.method == "POST":
        print(request.POST)
    return JsonResponse({"message": "success"})