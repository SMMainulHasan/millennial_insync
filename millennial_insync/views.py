from django.db.models import Count
from django.shortcuts import render

from article.models import Article, Category


def home(request):
    #REQUIREMENTS: show top 2 articles by ratings of each category
    #TODO: learn to do this in django query and update bellow
    categories = Category.objects.all()
    articles = []
    for category in categories:
        article_2 = category.article.all()[:2]
        articles.extend(article_2)
    return render(request, 'index.html', {'articles': articles})
