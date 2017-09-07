from django.shortcuts import render, redirect


# Create your views here.

def home(request):
   data = {}
   data['titulo'] = 'Dindri Delícia'
   return render(request, 'home.html', data)
