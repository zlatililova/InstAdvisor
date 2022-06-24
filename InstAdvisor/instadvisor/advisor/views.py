import logging
from django.shortcuts import get_object_or_404, render, redirect
from .models import Posts
from advisor.Forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .Forms import UserRegisterForm, ProfileUpdateForm


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('adivsor/profile.html')

    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        # 'p_form': p_form
    }
    return render(request, 'advisor/profile.html')


def searchbar(request):
    if request.method == 'GET':
        print("searchbars")
        search = request.GET.get('search')
        posts = Posts.objects.filter(title=search)
        return render(request, 'advisor/searchbar.html', {'posts': posts})
    return render(request, 'advisor/searchbar.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context = {"post": post}
    return render(request, "advisor/details.html", context)


def signinup(request):
    return render(request, 'advisor/signinup.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in!')
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'advisor/signup.html', {'form': form})


# Create your views here.
