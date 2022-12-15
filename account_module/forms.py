from django import forms
from django.core.exceptions import ValidationError


class Register_Form(forms.Form):
    email = forms.CharField(
        label="ایمیل",
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control form-control-lg",
                "id" : "form3Example3cg"
            }
        ),
    )
    password = forms.CharField(
        label="رمز عبور",
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "form3Example4"
            }
        )
    )
    repeat_password = forms.CharField(
        label="تکرار رمز عبور",
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "form3Example5"
            }
        )
    )


    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if(password == repeat_password):
            return repeat_password
        raise ValidationError("رمز عبور تطابق ندارد")