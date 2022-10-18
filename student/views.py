from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homest(request):
    return HttpResponse('welcome')


def loginfee(request):
    return render(request,'student_templates/login.html')