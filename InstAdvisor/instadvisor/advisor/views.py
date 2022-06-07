from django.shortcuts import render
from .schema import PostsMutation, Query, Mutation


def posts(request):
    context = {
        'posts': Query.resolve_all_posts(root=Query, info=any)
    }
    return render(request, 'advisor/posts.html', context)


def about(request):
    print(request.method)
    if request.method == "get":
        print("HERE!1!")
        id = request.GET.get('id')
        PostsMutation.mutate(root=Mutation, info=any,
                             title=None, execrpt=None, flag='delete', id=id)
        return render(request, 'advisor/aboutus.html')

    return render(request, 'advisor/aboutus.html')
    # return render(request, 'advisor/aboutus.html')


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


def profile(request):

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
