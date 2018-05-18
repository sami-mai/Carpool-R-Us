from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from . import views as driver_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/logout/$', auth_views.logout, {"next_page": '/'}),

]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
