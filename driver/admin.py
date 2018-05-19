from django.contrib import admin
from .models import Car, Driver_Profile, Location, Review, Tag


# Register your models here.
admin.site.register(Car)
admin.site.register(Driver_Profile)
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(Tag)
