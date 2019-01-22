from django.shortcuts import render

def home(request):
    return render(request, 'gorillacell/home.html')
