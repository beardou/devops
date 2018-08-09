from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# -*- coding: utf-8 -*-


# def base(request):
#     return HttpResponse("Hello World")

def base(request):
    return render(request, 'base.html', {})
