from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect


class LoginPageView(TemplateView):
    template_name = "login.html"


def logout_view(request):
    logout(request)
    return redirect('/')
