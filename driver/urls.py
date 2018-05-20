from django.conf.urls import url
from . import views as driver_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^home/(\d+)', driver_views.home, name='home'),
    url(r'^edit-profile/(\d+)', driver_views.edit_profile, name='edit_profile'),
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
