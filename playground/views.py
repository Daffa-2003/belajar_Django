from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sey_hello(request):
   return render(request, 'hello.html', {'name': 'Django'})
