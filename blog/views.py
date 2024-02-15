from django.shortcuts import render
from .serializers import ArticleSerializer,CategorySerializer
from .models import  Article,Category
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView




class ListArticleApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListACategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleDeleteApiView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryDeleteApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ArticleDetailApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateApiView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateApiView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


