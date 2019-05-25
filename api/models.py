from django.contrib.auth.models import User
from django.db import models


class ProfileManager(models.Manager):
    def filter_username(self, username):
        users = User.objects.filter(username=username)
        return super().get_queryset().filter(user=users[0])


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    about = models.CharField(max_length=100)

    objects = ProfileManager()

    def __str__(self):
        return "{} - {}".format(self.user, self.about)
