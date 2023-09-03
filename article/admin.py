from django.contrib import admin

from article.models import Article, Category, Review


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ('name', 'slug')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('headline',)}
    list_display = ('headline', 'slug', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)
