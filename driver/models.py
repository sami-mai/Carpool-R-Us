from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField


class Car(models.Model):
    type = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    colour = models.CharField(max_length=40)
    plate_num = models.DecimalField(decimal_places=2, max_digits=20)
    seats_available = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.plate_num

    class Meta:
        ordering = ['seats_available']


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(models.Model):
    '''
    reviews model class
    '''
    review = HTMLField(blank=True)
    driver = models.ForeignKey(User, related_name='driver_profile', on_delete=models.CASCADE, null=True)
    rider = models.ForeignKey(User, related_name='rider_profile', on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    @classmethod
    def get_reviews(cls, user_id):
        reviews = cls.objects.filter(user=user_id)
        return reviews


class Driver_Profile(models.Model):
    name = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    car_details = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_locations = models.ManyToManyField(Location, related_name='pickup')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(auto_now_add=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['destination']

    @receiver(post_save, sender=User)
    def update_driver_profile(sender, instance, created, **kwargs):
        if created:
            Driver_Profile.objects.create(user=instance)
        instance.driver_profile.save()
