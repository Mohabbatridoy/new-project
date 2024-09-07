from django.urls import path
from app1 import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('index/', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('account/',views.account, name="account"),
    
]