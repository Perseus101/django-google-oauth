from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings


class LoginPageView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject Google OAuth2 Client ID
        context['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'] = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        return context


def logout_view(request):
    logout(request)
    return redirect('/')
