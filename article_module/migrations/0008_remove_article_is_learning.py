# Generated by Django 4.0.6 on 2022-12-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0007_article_is_learning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_learning',
        ),
    ]