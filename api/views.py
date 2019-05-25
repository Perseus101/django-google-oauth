from rest_framework import viewsets

from api.serializers import ProfileSerializer
from api.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optionally filter profiles by username
        """
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = Profile.objects.filter_username(username)
        else:
            queryset = Profile.objects.all()
        return queryset
