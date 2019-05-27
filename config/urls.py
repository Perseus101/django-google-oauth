"""
URL Configuration
https://docs.djangoproject.com/en/2.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='auth-login'), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('auth-login/', include('authentication.urls'), name='auth'),
    path('auth/', include('rest_framework_social_oauth2.urls'), name='auth'),
    path('api/', include('api.urls'), name='profile'),
]

urlpatterns += staticfiles_urlpatterns()
