from django.urls import path
from .views import ArticleCreateApiView,ArticleDeleteApiView,ArticleUpdateApiView,\
    ArticleDetailApiView,CategoryDeleteApiView,ListArticleApiView,ListACategoryApiView

urlpatterns = [
    path('api/v1/articlelist/',ListArticleApiView.as_view()),
    path('api/v1/categorylist/',ListACategoryApiView.as_view()),
    path('api/v1/createarticle/',ArticleCreateApiView.as_view()),
    path('api/v1/deletearticle/<int:pk>/',ArticleDeleteApiView.as_view()),
    path('api/v1/deletecategory/<int:pk>/',CategoryDeleteApiView.as_view()),
    path('api/v1/detailarticle/<int:pk>/',ArticleDetailApiView.as_view()),
    path('api/v1/updatearticle/<int:pk>/',ArticleUpdateApiView.as_view()),
]
