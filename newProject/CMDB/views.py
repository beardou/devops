from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from CMDB.models import *


# Create your views here.
# -*- coding: utf-8 -*-


# def base(request):
#     return HttpResponse("Hello World")

def base(request):
    Employees = Employee.objects.all()
    return render(request, 'base.html', {'Employees': Employees})
