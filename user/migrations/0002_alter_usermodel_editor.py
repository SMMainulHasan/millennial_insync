# Generated by Django 4.2.3 on 2023-09-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='editor',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]