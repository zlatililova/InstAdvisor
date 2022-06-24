from django.shortcuts import render, redirect

from .userSchema import AuthMutation
from .schema import PostsMutation, Query, Mutation
from advisor.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileUpdateForm

def posts(request):
    context = {
        'posts': Query.resolve_all_posts(root=Query, info=any)
    }
    return render(request, 'advisor/posts.html', context)


def about(request):
    # print(request.method)
    # if request.method == "get":
    #     print("HERE!1!")
    #     id = request.GET.get('id')
    #     PostsMutation.mutate(root=Mutation, info=any,
    #                          title=None, execrpt=None, flag='delete', id=id)
    #     return render(request, 'advisor/aboutus.html')

    # return render(request, 'advisor/aboutus.html')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        AuthMutation.register()
        return render(request, 'advisor/aboutus.html')

    return render(request, 'advisor/aboutus.html')


def home(request):
    return render(request, 'advisor/index.html')


def newpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        execrpt = request.POST.get('execrpt')
        PostsMutation.mutate(root=Mutation, info=any, title=title,
                             execrpt=execrpt, flag='create', id=None)
        return render(request, 'advisor/newpost.html')

    return render(request, 'advisor/newpost.html')


def search(request):
    return render(request, 'advisor/search.html')


def profile1(request):

    # print(request.method)
    # print(request)
    # if "delete" in request.GET:
    #     print("delete")
    if request.method == "GET" and "delete" in request.GET:
        print("into delete")
        id = request.GET.get('id')
        PostsMutation.mutate(root=Mutation, info=any,
                             title=None, execrpt=None, id=id, flag='delete')
        return render(request, 'advisor/profile.html')

    elif request.method == "GET":  # and "update" in request:
        print("into update")
        title = request.GET.get('title')
        execrpt = request.GET.get('execrpt')
        id = request.GET.get('id')
        PostsMutation.mutate(root=Mutation, info=any,
                             title=title, execrpt=execrpt, id=id, flag='update')
        return render(request, 'advisor/profile.html')

    return render(request, 'advisor/profile.html')


def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        posts = Query.resolve_filter_posts(root=Query, info=any, search=search)
    return render(request, 'advisor/searchbar.html', {'posts': posts})


def details(request):
    return render(request, 'advisor/details.html')


def signinup(request):
    return render(request, 'advisor/signinup.html')

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

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
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profiles.html')

