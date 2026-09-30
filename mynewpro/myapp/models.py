from django.db import models


class UserProfile(models.Model):
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )