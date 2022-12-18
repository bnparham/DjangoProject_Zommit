from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, ArticleCategory
# Create your views here.

class body_main_sideView(ListView):
    model = Article
    template_name = "article_module/body_components/main_side.html"


def header_main_menuView(request:HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        "main_categories": article_main_categories
    }
    return render(request, "article_module/header_components/main-menu.html", context)