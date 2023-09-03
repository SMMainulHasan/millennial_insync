from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse

from article.forms import ArticleCreateForm
from article.models import Article, Category, Review


#Create or post article 
def create_article(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            data = Article()
            data.writer = request.user
            data.headline = request.POST.get('headline')
            data.tags = request.POST.get('tags')
            data.body = request.POST.get('body')
            data.img = request.POST.get('img')
            data.category = form.cleaned_data['category']
            data.save()
            return redirect("home")
        
    return render(request, 'article/create_article.html', {'form': form})

#Update or post article 
def create_article(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            data = Article()
            data.writer = request.user
            data.headline = request.POST.get('headline')
            data.tags = request.POST.get('tags')
            data.body = request.POST.get('body')
            data.img = request.POST.get('img')
            data.category = form.cleaned_data['category']
            data.save()
            return redirect("home")
        
    return render(request, 'article/create_article.html', {'form': form})

#Category wise article view all
def category_article_view(request, category_slug):
    articles = Article.objects.filter(category__slug = category_slug)
    return render(request, 'article/category.html', {'articles': articles})

    
#Article Detail view
def article_detail(request, category_slug, article_slug):
    article = Article.objects.get(slug = article_slug)
    avg_raging = Review.objects.filter(article = article).aggregate(avg_raging=Avg('rating'))['avg_raging']
    return render(request, 'article/article_detail.html', {'article': article, 'avg_raging':avg_raging})


#This takes user ratings only 
#TODO: take reviews also after exam
def review_rating(request):
    if request.method == "POST":
        article_slug = request.POST.get('article_slug')
        rating = request.POST.get('rate')
        article = Article.objects.get(slug = article_slug)
        data = Review()
        data.user = request.user
        data.article = article
        data.rating = rating
        data.save()

        #doing this to redirect in same page
        category_slug = article.category.slug
        article_slug = article.slug
        dynamic_url = reverse('article_detail', args=[category_slug,article_slug])
        return redirect(dynamic_url)
