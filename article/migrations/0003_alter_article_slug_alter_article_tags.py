# Generated by Django 4.2.3 on 2023-09-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_category_alter_article_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
