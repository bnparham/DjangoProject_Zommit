from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from account_module.forms import Register_Form


class RegisterView(View):
    def get(self,request):
        register_form = Register_Form()
        context = {
            "register_form" : register_form
        }
        return render(request, "account_module/register_page.html", context)
    def post(self,request):
        register_form = Register_Form(request.POST)
        context = {
            "register_form": register_form
        }
        if(register_form.is_valid()):
            print(register_form.cleaned_data)
            return redirect(reverse("home-page"))
        return render(request, "account_module/register_page.html", context)