from django.shortcuts import render
from .schema import Query, schema

def posts(request):
    context= {
        'posts': Query.resolve_all_posts(root = Query, info=any)
    }
    return render(request, 'advisor/posts.html', context)

def about(request):
    return render(request, 'advisor/aboutus.html')

def home(request):
    return render(request, 'advisor/index.html')

def newpost(request):
    return render(request, 'advisor/newpost.html')

def search(request):
    return render(request, 'advisor/search.html')

def profile(request):
    return render(request, 'advisor/profile.html')

def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        
        posts = Query.filter_posts(root = Query, info=any, title = search)
        
    return render(request, 'advisor/searchbar.html', {'posts': posts})

# Create your views here.
