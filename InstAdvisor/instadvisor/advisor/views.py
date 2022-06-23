from django.shortcuts import render
from .models import Posts
from .Forms import UploadFileForm


def posts(request):
    posts = Posts.objects.all()
    dictionary = {"posts": posts}
    return render(request, "advisor/posts.html", dictionary)


def about(request):

    return render(request, 'advisor/aboutus.html')


def home(request):
    return render(request, 'advisor/index.html')


def handle_uploaded_file(f):
    with open("media/" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def newpost(request):
    if request.method == "POST":
        print(request.FILES)
        object1 = Posts(title=request.POST.get("title"),
                        text=request.POST.get("text"),
                        image=request.FILES.get("image").name,
                        )
        object1.save()
        handle_uploaded_file(request.FILES["image"])
        return render(request, "advisor/posts.html")
    return render(request, "advisor/newpost.html")


def search(request):
    return render(request, 'advisor/search.html')


def profile(request):

    return render(request, 'advisor/profile.html')


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Posts.objects.filter(title=search)
        return render(request, 'advisor/searchbar.html', {'posts': posts})


def details(request):
    return render(request, 'advisor/details.html')


def signinup(request):
    return render(request, 'advisor/signinup.html')


def signin(request):
    return render(request, 'advisor/signin.html')


def signup(request):
    return render(request, 'advisor/signup.html')


def details(request):
    return render(request, 'advisor/details.html')


# Create your views here.
