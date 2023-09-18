from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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


# Create Profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)
