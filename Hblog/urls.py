from django.urls import path
# from . import views
from .views import Homeview, ArticleDetailView, AddPostView, UpdatePostview, DeletePostView, AddCategoryView, CategoryView, SearchArticle, LikeView, DislikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Homeview.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostview.as_view(), name='edit_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:categories>', CategoryView, name='category'),
    path('search_article/', SearchArticle, name='search-article'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('dislike/<int:pk>', DislikeView, name='dislike_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
  