from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from .models import Article, ArticleCategory
# Create your views here.
from home_module.views import HomePageView

class RedirectHome(View):
    def get(self, request):
        return redirect(reverse("home-page"))

class body_main_sideView(ListView):
    model = Article
    template_name = "article_module/body_components/homePage/main_side-home.html"
    paginate_by = 8

    def get_queryset(self):
        query = super(body_main_sideView, self).get_queryset()
        query = query.order_by("-create_date")
        category_name = self.kwargs.get("category")
        if(category_name is not None):
            query = query.filter(selected_categories__url_title__iexact=category_name, is_active=True)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(body_main_sideView, self).get_context_data()
        url_title = self.kwargs.get("category", None)
        if(url_title):
            title = ArticleCategory.objects.filter(url_title=url_title).values("title")[0].get("title")
            context["url_persian_title"] = title
        return context

class detailPageView(DetailView):
    model = Article
    template_name = "article_module/body_components/detailPage/main_side-details.html"


class body_right_sideView(ListView):
    # most-view articles
    model = Article
    template_name = "article_module/body_components/homePage/right_side.html"

    def get_queryset(self):
        query = super(body_right_sideView, self).get_queryset()
        query = query.order_by("-view_count")[:5]
        return query

class body_left_sideView(ListView):
    model = Article
    template_name = "article_module/body_components/homePage/left_side.html"
    
    def get_queryset(self):
        query = super(body_left_sideView, self).get_queryset()
        query = query.filter(selected_categories__url_title__iexact="howto")[:5]
        return query



def header_main_menuView(request:HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        "main_categories": article_main_categories
    }
    return render(request, "article_module/header_components/main-menu.html", context)