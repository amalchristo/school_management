from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('homepage')

def loginfun(request):
    return render(request,'teacher_templates/login.html')

def signupfun(request):
    return render(request,'teacher_templates/signup.html')

def welcome(request):
    return render(request,'teacher_templates/welcome.html')