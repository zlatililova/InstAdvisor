import imp
from inspect import ismethoddescriptor
from operator import contains
from turtle import title
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from .models import Posts
import django_filters
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

class PostsFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    title = django_filters.CharFilter(lookup_expr=['icontains'])

    class Meta:
        model = Posts
        fields = ['title', 'id', 'execrpt']

class Query(graphene.ObjectType):

    post = relay.Node.Field(PostsType)
    all_posts = DjangoFilterConnectionField(PostsType, filterset_class=PostsFilter)
    #def resolve_all_posts(root, info, **kwargs):

    def resolve_all_posts(root, info, search=None):
        queryset = Posts.objects.all()
        if search: 
            queryset = queryset.filter(title__icontains=search)

        return queryset
    

schema =  graphene.Schema(query=Query)   

