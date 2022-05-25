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

    def resolve_all_posts(root, info):
        return Posts.objects.filter(title="Test post")

schema =  graphene.Schema(query=Query)   
