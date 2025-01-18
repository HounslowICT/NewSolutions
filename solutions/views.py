from django.shortcuts import render
from django.http import HttpResponse



def homepage1(request):
    return HttpResponse('index.html')


