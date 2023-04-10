from django.shortcuts import render
from app.models import *

# Create your views here.
def display_dept(request):
    loe=Dept.objects.all()
    d={'loe':loe}
    return render(request,'display_dept.html',d)

def display_emp(request):
    loe=Emp.objects.all()
    d={'loe':loe}
    return render(request,'display_emp.html',d)