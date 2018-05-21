from django.conf.urls import url
# from . import views as geo_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # url(r'^map/', views.home, name='home'),

]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
