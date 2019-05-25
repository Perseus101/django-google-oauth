from django.urls import include, path
from authentication import views

app_name = 'auth'
urlpatterns = [
    # Notice the URL has been named
    path('', views.LoginPageView.as_view(), name='login'),
    path('', include('social_django.urls', namespace='social')),
    path('logout', views.logout_view, name='logout'),
]
