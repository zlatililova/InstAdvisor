from django.urls import path
import graphql
from . import views
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from .schema import schema as s
from .userSchema import schema as us
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=s)), 
    path("ugraphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=us))),
    path("posts/", views.posts, name = 'posts'),
    path('', views.home, name='home'),
    path("aboutus/", views.about, name = 'about us'),
    path("posts/", views.posts, name = 'posts'),
    path("newpost/", views.newpost, name = 'new post'),
    path("search/", views.search, name = 'search'),
    path("profile/", views.profile, name = 'profile'),
    path("searchbar/", views.searchbar, name="searchbar"),
    path("details/", views.details, name="details"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''path('', views.home, name='home'),
    path("aboutus/", views.about, name = 'about us'),
    path("posts/", views.posts, name = 'posts'),
    path("newpost/", views.newpost, name = 'new post'),
    path("search/", views.search, name = 'search'),
    path("profile/", views.profile, name = 'profile'),'''