from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Article, ArticleCategory
# Create your views here.
from home_module.views import HomePageView

class body_main_sideView(ListView):
    model = Article
    template_name = "article_module/body_components/main_side.html"

    def get_queryset(self):
        query = super(body_main_sideView, self).get_queryset()
        category_name = self.kwargs.get("category")
        if(category_name is not None):
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class body_right_sideView(TemplateView):
    template_name = "article_module/body_components/right_side.html"

class body_left_sideView(TemplateView):
    template_name = "article_module/body_components/left_side.html"



def header_main_menuView(request:HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        "main_categories": article_main_categories
    }
    return render(request, "article_module/header_components/main-menu.html", context)