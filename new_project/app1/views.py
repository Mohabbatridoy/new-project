from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>be patiance, be honest, be dedicated</h1>")
def home(request):
    return HttpResponse("<h1> this is for home page</h1>")
def contact(request):
    return HttpResponse("this is contact page")
def account(request):
    return HttpResponse("this is account page")