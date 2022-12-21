# Generated by Django 4.0.6 on 2022-12-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_article_is_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_article',
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='is_article',
            field=models.BooleanField(default=True, verbose_name='مقاله میباشد'),
        ),
    ]