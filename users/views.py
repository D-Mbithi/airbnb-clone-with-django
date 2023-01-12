from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from . import forms


# Create your views here.
class LoginView(View):
    """Login View defined"""

    def get(self, request):
        form = forms.LoginForms()
        template = "users/login.html"
        context = {
            "form": form,
        }
        return render(request, template, context)

    def post(self, request):
        form = forms.LoginForms(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        template = "users/login.html"
        context = {
            "form": form,
        }

        return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect(reverse("users:login"))
