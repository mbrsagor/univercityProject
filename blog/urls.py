from django.urls import pathfrom blog.views.article_views import *from blog.views.book_views import PublisherList, PublisherDetailurlpatterns = [    path('', ArticleListView.as_view(), name='article_list'),    path('create-article/', CreateArticleView.as_view(), name='create_article'),    path('article/detail/<title>', DetailView.as_view(), name='detail'),    path('publishers/', PublisherList.as_view()),    path('publishers/<int:id>/', PublisherDetail.as_view()),]