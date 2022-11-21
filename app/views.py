from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def wish(request):
    return HttpResponse('this is my first function')
