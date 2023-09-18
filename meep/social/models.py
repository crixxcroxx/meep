from django.db import models
from django.contrib.auth.models import User


# Create User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,  # if you follow someone they're NOT required to follow you back
        blank=True,  # you're not required to follow anyone
    )

    def __str__(self):
        return self.user.username
