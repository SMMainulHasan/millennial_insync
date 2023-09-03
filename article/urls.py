from django.urls import path

from article.views import (article_detail, category_article_view,
                           create_article, delete_article, edit_article,
                           profile, review_rating)

urlpatterns = [
    path("profile/", profile, name='profile'),
    path("create/", create_article, name='create_article'),
    path("edit/<slug:article_slug>/", edit_article, name='edit_article'),
    path("delete/<slug:article_slug>/", delete_article, name='delete_article'),
    path("category/<slug:category_slug>/", category_article_view, name='category_article'),
    path("category/<slug:category_slug>/<slug:article_slug>/", article_detail, name='article_detail'),
    path("rate/", review_rating, name='review_rating'),
]
