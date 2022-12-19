from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home_module/homePage.html"

class ConatctUsView(TemplateView):
    template_name = "home_module/contactUs.html"



def HeaderSection_Component(req):
    return render(req, "shared/header_section.html")


def FooterSection_Component(req):
    return render(req, "shared/footer_section.html")


class GridItemSection_Component(TemplateView):
    template_name = "shared/gridItem_section.html"

class FeatureNewsSection_Component(TemplateView):
    template_name = "shared/featureNews_section.html"

class BodySection_Component(TemplateView):
    template_name = "shared/body_section.html"

class GuidSection_Component(TemplateView):
    template_name = "shared/guid_section.html"

class ReviewSection_Component(TemplateView):
    template_name = "shared/review_section.html"
# --- layout components ----
