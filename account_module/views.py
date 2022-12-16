from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views import View

from account_module.forms import Register_Form,Login_Form


class RegisterView(View):
    def get(self, request):
        register_form = Register_Form()
        context = {
            "register_form": register_form
        }
        return render(request, "account_module/register_page.html", context)

    def post(self, request):
        register_form = Register_Form(request.POST)
        print(f"POST is {request.POST}")
        if(register_form.is_valid()):
            print(register_form.cleaned_data)
            return redirect(reverse("home-page"))
        context = {
            "register_form": register_form
        }
        return render(request, "account_module/register_page.html", context)

class LoginVeiw(View):
    def get(self, request):
        login_form = Login_Form()
        context = {
            "login_form": login_form
        }
        return render(request, "account_module/login_page.html", context)

    def post(self, request):
        login_form = Login_Form(request.POST)
        print(f"POST is {request.POST}")
        if(login_form.is_valid()):
            print(login_form.cleaned_data)
            return redirect(reverse("home-page"))
        context = {
            "login_form": login_form
        }
        return render(request, "account_module/login_page.html", context)