from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    #path("create/", views.create, name = "create-post"),
    path("aboutus/", views.about, name = 'about us'),
    path("posts/", views.posts, name = 'posts'),
    path("newpost/", views.newpost, name = 'new post'),
    path("search/", views.search, name = 'search'),
    path("signinup/", views.signinup, name = 'signinup'),
    path("profile/", views.profile, name = 'profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)