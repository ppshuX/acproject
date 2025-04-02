from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def template1(request):
    return render(request, 'template1.html')

def template2(request):
    return render(request, 'template2.html')

def template3(request):
    return render(request, 'template3.html')

def template4(request):
    return render(request, 'template4.html')

def kob(request):
    return render(request, 'kobrule.html')