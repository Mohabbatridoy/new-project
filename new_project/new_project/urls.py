
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' /',views.index, name='index'),
    path('home/',views.index, name='index'),
    path('index/', views.index, name="index"),
    path('m2/',views.index, name="index"),
]
