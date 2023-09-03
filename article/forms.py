from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ChoiceField, ModelForm, Textarea, TextInput

from article.models import Article


class ArticleCreateForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['headline', 'tags','category', 'body', 'img']

        widgets = {
            'headline': TextInput(attrs={'class':("form-control")}),
            'tags': TextInput(attrs={'class':("form-control")}),
            'body': Textarea(attrs={'class':('form-control')}),
        }
