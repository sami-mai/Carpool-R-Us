from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from driver.models import Location, Review


class Rider_Profile(models.Model):
    name = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(Location, related_name='pickup', on_delete=models.CASCADE)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    national_ID = models.DecimalField()
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pickup_location']

    @receiver(post_save, sender=User)
    def update_rider_profile(sender, instance, created, **kwargs):
        if created:
            Rider_Profile.objects.create(user=instance)
        instance.rider_profile.save()
