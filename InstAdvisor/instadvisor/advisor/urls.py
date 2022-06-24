from django.urls import path
import graphql
from . import views
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
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
    #path("signin/", views.signin, name='signin'),
    path('signin/', auth_views.LoginView.as_view(template_name='advisor/signin.html'), name='signin'),
    path("signup/", views.signup, name='signup'),
    path("posts/<int:post_id>/", views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''path('', views.home, name='home'),
    path("aboutus/", views.about, name = 'about us'),
    path("posts/", views.posts, name = 'posts'),
    path("newpost/", views.newpost, name = 'new post'),
    path("search/", views.search, name = 'search'),
    path("profile/", views.profile, name = 'profile'),'''
