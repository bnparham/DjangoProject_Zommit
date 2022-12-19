from django.urls import path
from .views import *

urlpatterns = [
    path("contact-us", ConatctUsView.as_view(), name="contactUs-page")
]