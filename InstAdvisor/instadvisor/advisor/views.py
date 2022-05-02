from django.shortcuts import render

def home(request):
    return render(request, 'advisor/index.html')

def about(request):
    return render(request, 'advisor/aboutus.html')

# Create your views here.
