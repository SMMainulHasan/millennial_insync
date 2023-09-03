from django.urls import path

from article.views import (article_detail, category_article_view,
                           create_article, review_rating)

urlpatterns = [
    path("create/" , create_article, name='create_article'),
    path("category/<slug:category_slug>/" , category_article_view, name='category_article'),
    path("category/<slug:category_slug>/<slug:article_slug>/" , article_detail, name='article_detail'),
    path("rate/" , review_rating, name='review_rating'),
]
