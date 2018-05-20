from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from driver.models import Location, Review


class Rider_Profile(models.Model):
    name = models.OneToOneField(User, related_name='rider_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(Location, related_name='rider_pickup', on_delete=models.CASCADE)
    reviews = models.ForeignKey(Review, related_name='rider_review', on_delete=models.CASCADE)
    national_ID = models.DecimalField(decimal_places=2, max_digits=50)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pickup_location']
