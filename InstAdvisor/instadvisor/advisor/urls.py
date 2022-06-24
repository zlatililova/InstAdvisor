from django.urls import path
import graphql
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .schema import schema as s
from django.contrib import admin
from django.urls import path, include
from advisor import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=s)),
    path("posts/", views.posts, name='posts'),
    path('', views.home, name='home'),
    path("aboutus/", views.about, name='about us'),
    path("posts/", views.posts, name='posts'),
    path("newpost/", views.newpost, name='new post'),
    path("search/", views.search, name='search'),
    path("profile/", views.profile, name='profile'),
    path("searchbar/", views.searchbar, name="searchbar"),
    path("details/", views.details, name="details"),
    path("signinup/", views.signinup, name='signinup'),
    
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name= 'users/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html')),

    
]

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

