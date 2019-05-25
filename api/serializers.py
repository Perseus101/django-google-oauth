from rest_framework import serializers

from api.models import Profile


class UserField(serializers.RelatedField):
    def to_representation(self, user):
        return user.username


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'about')
