from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings

from oauth2_provider.models import Application

class LoginPageView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject Google OAuth2 Client ID
        context['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'] = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        context['SOCIAL_AUTH_CLIENT_ID'] = Application.objects.all()[0].client_id
        return context


def logout_view(request):
    logout(request)
    return redirect('/')
