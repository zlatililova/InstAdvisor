from operator import pos
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from .models import Posts
import django_filters

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

class PostsMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        execrpt = graphene.String()
        id = graphene.ID()

    posts = graphene.Field(PostsType)

    @classmethod
    def mutate(cls, root, info, title, execrpt, id, flag):
        if flag == 'create':
            posts = Posts(title=title, execrpt = execrpt)
            posts.save()
        elif flag == 'update':
            try:
                posts = Posts.objects.get(id=id)
            except Posts.DoesNotExist:
                posts = None
                return 
            if title:
                posts.title = title
            if execrpt:
                posts.execrpt = execrpt
            posts.save()
        else:
            posts = Posts.objects.get(id=id)
            posts.delete()

        return PostsMutation(posts=posts)




class Query(graphene.ObjectType):

    post = relay.Node.Field(PostsType)
    filter_posts = DjangoFilterConnectionField(PostsType, filterset_class=PostsFilter)
    all_posts = graphene.List(PostsType)
    #def resolve_all_posts(root, info, **kwargs):

    def resolve_filter_posts(root, info, search=None):
        queryset = Posts.objects.all()
        if search: 
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def resolve_all_posts(root, info):
        return Posts.objects.all()

class Mutation(graphene.ObjectType):
    create_posts =  PostsMutation.Field()





schema =  graphene.Schema(query=Query, mutation=Mutation)   

