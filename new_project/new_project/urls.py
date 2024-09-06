
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('/',views.index, name='index'),
    path('index/', views.index, name="index"),
    path('m2/',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('home/',views.home, name="home"),
    path('account/', views.account, name="account"),
]
