from django.db.models import Avg, Count
from django.shortcuts import render

from article.models import Article, Category, Review


#REQUIREMENTS: show top 2 articles by ratings of each category
def home(request):
    #TODO: learn to do this in django query and update bellow (Full query to learn)
    categories = Category.objects.all()
    articles = []
    for category in categories:
        articles_by_category = category.article.all()
        articles_avg_rating_annotated = articles_by_category.annotate(avg_rating=Avg('review__rating'))
        sorted_articles = articles_avg_rating_annotated.order_by('-avg_rating')[:2]
        articles.extend(sorted_articles)
    return render(request, 'index.html', {'articles': articles})
