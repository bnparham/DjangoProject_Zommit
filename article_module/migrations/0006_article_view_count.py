# Generated by Django 4.0.6 on 2022-12-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0005_remove_article_is_article_articlecategory_is_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
