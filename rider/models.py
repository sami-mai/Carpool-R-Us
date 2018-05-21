from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from driver.models import Location, Review


class Rider_Profile(models.Model):
    name = models.OneToOneField(User, related_name='rider_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE, null=True)
    pickup_location = models.ForeignKey(Location, related_name='rider_pickup', on_delete=models.CASCADE, null=True)
    reviews = models.ForeignKey(Review, related_name='rider_review', on_delete=models.CASCADE, null=True)
    national_ID = models.CharField(max_length=40, null=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pickup_location']

    # Create Profile when creating a User
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Rider_Profile.objects.create(name=instance)
        instance.profile.save()
