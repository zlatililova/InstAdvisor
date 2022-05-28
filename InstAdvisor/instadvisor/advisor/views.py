from django.shortcuts import render
from .schema import PostsMutation, Query, Mutation

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
        
        posts = Query.resolve_filter_posts(root = Query, info=any, search = search)
        
    return render(request, 'advisor/searchbar.html', {'posts': posts})

def details(request):
    if request.method == "POST":
        mute =PostsMutation()
        title = request.POST.get('title')
        execrpt = request.POST.get('execrpt')
        
        posts = mute.mutate(root = Mutation, info = any, title=title, execrpt = execrpt)
        
    return render(request, 'advisor/details.html', {'posts': posts})

# Create your views here.
