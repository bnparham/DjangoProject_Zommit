from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
# Create your views here.

class body_main_sideView(ListView):
    model = Article
    template_name = "shared/body_components/main_side.html"


