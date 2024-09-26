from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Musician, Album

# Create your views here.

def index(request):
    Musician_list = Musician.objects.order_by("first_name")
    diction = {'text1': 'This is the list of Musician', 'musician': Musician_list}
    return render(request, 'app1/index.html', context= diction)
