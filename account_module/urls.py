from django.urls import path

from .views import *

urlpatterns = [
    path("register", RegisterView.as_view(), name="register_page"),
    path("login", LoginVeiw.as_view(), name="login_page"),
]