from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet, 'Profile')

app_name = 'profile'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
