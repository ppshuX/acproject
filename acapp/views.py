from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def template1(request):
    return render(request, 'template1.html')

def template2(request):
    return render(request, 'template2.html')