from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  #the path for our index view
    path('password/', views.password, name="password"),
    path('about/', views.about, name="about"),
]