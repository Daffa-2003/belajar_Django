from django.urls import path 
from . import views

# URL Configuration for the playground app
urlpatterns = [
    path('hello/', views.sey_hello)
]