from django.shortcuts import render

def home(request):
    return render(request, 'advisor/index.html')

def about(request):
    return render(request, 'advisor/aboutus.html')

def posts(request):
    return render(request, 'advisor/posts.html')

def newpost(request):
    return render(request, 'advisor/newpost.html')

def search(request):
    return render(request, 'advisor/search.html')

def signinup(request):
    return render(request, 'advisor/signinup.html')

def profile(request):
    return render(request, 'advisor/profile.html')

# Create your views here.
