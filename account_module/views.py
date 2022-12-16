from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string

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
            user_email = register_form.cleaned_data.get("email")
            user : bool = User.objects.filter(email__iexact=user_email).exists()
            if(user):
                register_form.add_error("email", "ایمیل وارد شده متعلق به حساب کاربری دیگری میباشد")
            else:
                user_pass = register_form.cleaned_data.get("password")
                new_user = User(
                    email=user_email,
                    is_active=False,
                    email_activation_code=get_random_string(72),
                )
                new_user.set_password(user_pass)
                new_user.save()
                request.session["register_msg"] = True
                #todo : send user activition code
                return redirect(reverse("login_page"))
        context = {
            "register_form": register_form
        }
        return render(request, "account_module/register_page.html", context)

class LoginVeiw(View):
    def get(self, request):
        login_form = Login_Form()
        register_msg = request.session.get("register_msg", False)
        if(register_msg): del(request.session["register_msg"])
        context = {
            "login_form": login_form,
            "register_msg": register_msg
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