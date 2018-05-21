from django.conf.urls import url
from . import views as rider_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^home/(\d+)', rider_views.home, name='rider_home'),
    url(r'^edit-profile/(\d+)', rider_views.edit_profile, name='edit_riderprofile'),
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
