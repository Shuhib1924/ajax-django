from django.shortcuts import render
from .models import Employee, Office, OfficeForm, EmployeeForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
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
        officeForm = OfficeForm(request.POST)
        office = officeForm.save()
    return JsonResponse(model_to_dict(office), safe=False)