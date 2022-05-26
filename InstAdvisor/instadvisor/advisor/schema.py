from turtle import title
import graphene
from graphene_django import DjangoObjectType
from .models import Posts

class PostsType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ("id", "title", "execrpt")



class Query(graphene.ObjectType):

    all_posts = graphene.List(PostsType)
    filter_posts = graphene.Field(PostsType, id = graphene.Int())

    def resolve_all_posts(root, info):
        return Posts.objects.all()
    
    # def filter_posts(root, info, title):
    #     return Posts.objects.filter(title = title)
    def filter_posts(root, info, title=None, **kwargs):
        if title:
            filter = (
                Posts(title__icontains=title) |
                Posts(description__icontains=title)
            )
            return Posts.objects.filter(filter)

        return Posts.objects.all()

schema =  graphene.Schema(query=Query)   
