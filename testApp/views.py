from django.shortcuts import render

def helloDjango(request):
    return render(request, 'hello.html')

def homePage(request):
    return render(request, "header.html")