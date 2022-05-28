import imp
from inspect import ismethoddescriptor
from turtle import title
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from .models import Posts
from django.db.models import QuerySet

class PostsType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ("id", "title", "execrpt")
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
            'execrpt': ['exact'],
        }
        interfaces = (relay.Node, )



class Query(graphene.ObjectType):



    post = relay.Node.Field(PostsType)
    all_posts = DjangoFilterConnectionField(PostsType)

    #def resolve_all_posts(root, info, **kwargs):

    def resolve_all_posts(root, info, search=None):
        queryset = Posts.objects.all()
        if search:
            
            queryset = queryset.filter(filter='icontains', search=search)

        return queryset
    

schema =  graphene.Schema(query=Query)   

