from django.urls import path

from home_module.views import HomePageView
from .views import *
urlpatterns = [
    path('', body_main_sideView.as_view(), name="home-page"),
    path('articles', RedirectHome.as_view(), name="redirect-home_articles"),
    path('articles/cat', RedirectHome.as_view(), name="redirect-home_cat"),
    path('articles/cat/zommit', RedirectHome.as_view(), name="redirect-home_zommit"),
    path("articles/cat/<str:category>", body_main_sideView.as_view(), name="home-page-by-category"),
    path("articles/<slug:slug>", detailPageView.as_view(), name="detail-page"),
]