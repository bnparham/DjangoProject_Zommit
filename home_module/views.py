from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from article_module.models import Article

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home_module/homePage.html"

class ConatctUsView(TemplateView):
    template_name = "home_module/contactUs.html"



def HeaderSection_Component(req):
    return render(req, "shared/header_section.html")


def FooterSection_Component(req):
    return render(req, "shared/footer_section.html")


class GridItemSection_Component(ListView):
    model = Article
    template_name = "shared/gridItem_section.html"

    def get_queryset(self):
        query = super(GridItemSection_Component, self).get_queryset()
        query = query.filter(is_slider=True).order_by("title")[:5]
        return query

class FeatureNewsSection_Component(ListView):
    model = Article
    template_name = "shared/featureNews_section.html"

    def get_queryset(self):
        query = super(FeatureNewsSection_Component, self).get_queryset()
        query = query.filter(is_suggest=True)[:5]
        return query

class BodySection_Component(TemplateView):
    template_name = "shared/body_section.html"

class GuidSection_Component(ListView):
    model = Article
    template_name = "shared/guid_section.html"
    def get_queryset(self):
        query = super(GuidSection_Component, self).get_queryset()
        query = query.filter(selected_categories__url_title__iexact="buying-guide")[:6]
        return query

class ReviewSection_Component(ListView):
    model = Article
    template_name = "shared/review_section.html"
    
    def get_queryset(self):
        query = super(ReviewSection_Component, self).get_queryset()
        query = query.filter(selected_categories__url_title__iexact="review").order_by("-create_date")[:6]
        return query

# --- layout components ----
