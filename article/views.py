from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse

from article.forms import ArticleCreateForm, ArticleEditForm
from article.models import Article, Category, Review


#PROFILE VIEW
def profile(request):
    articles = Article.objects.filter(writer=request.user)
    return render(request, 'article/profile.html', {'articles':articles})


# <<<============= CRUD OPERATION START ===================>>>

#Create or post article 
def create_article(request):
    if request.user.UserModel.editor:
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
                return redirect("profile")
        return render(request, 'article/create_article.html', {'form': form})
    else:    
        return render(request, 'article/not_accessible.html')

#Update or edit article 
def edit_article(request, article_slug):
    if request.user.UserModel.editor:
        article = Article.objects.get(slug = article_slug)
        form = ArticleEditForm(instance=article)
        if request.method == 'POST':
            edited_article = ArticleEditForm(request.POST, instance=article)
            if edited_article.is_valid():
                edited_article.save()
                return redirect("profile")
            
        return render(request, 'article/edit_article.html', {'form': form})
    else:    
        return render(request, 'article/not_accessible.html')

#delete article 
def delete_article(request, article_slug):
    if request.user.UserModel.editor:
        article = Article.objects.get(slug = article_slug)
        article.delete()
        return redirect("profile")
    else:    
        return render(request, 'article/not_accessible.html')

# <<<============= CRUD OPERATION END ===================>>>


#Category wise article view all
def category_article_view(request, category_slug):
    articles = Article.objects.filter(category__slug = category_slug)
    #Sorted by article Ratings
    articles_avg_rating_annotated = articles.annotate(avg_rating=Avg('review__rating'))
    sorted_articles = articles_avg_rating_annotated.order_by('-avg_rating')
    return render(request, 'article/category.html', {'articles': sorted_articles})

    
#Article Detail view
def article_detail(request, category_slug, article_slug):
    article = Article.objects.get(slug = article_slug)
    avg_raging = Review.objects.filter(article = article).aggregate(avg_raging=Avg('rating'))['avg_raging']

    articles = Article.objects.filter(category__slug = category_slug).exclude(slug=article_slug)[:2]
    categories = Category.objects.all()
    return render(request, 'article/article_detail.html', {'article': article,'articles':articles, 'avg_raging':avg_raging, 'categories': categories})


#This takes user ratings only 
#TODO: implement comment also after exam
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
