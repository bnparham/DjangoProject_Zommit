from django.urls import path

from home_module.views import HomePageView
from .views import *
urlpatterns = [
    path('', body_main_sideView.as_view(), name="home-page"),
    path("articles/cat/<str:category>", body_main_sideView.as_view(), name="home-page-by-category"),
]