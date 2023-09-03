from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    img = models.FileField(blank=True, null=True, upload_to="photos/category")

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    tags = models.CharField(max_length=500,blank=True, null=True)
    category = models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE)
    body = models.TextField()
    img = models.FileField(blank=True, null=True, upload_to="photos/article")
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    published_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.headline
    
class Review(models.Model):
    article = models.ForeignKey(Article, related_name='review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True)
    
