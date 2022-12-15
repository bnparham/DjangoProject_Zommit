from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("contact-us", ConatctUsView.as_view(), name="contactUs-page")
]