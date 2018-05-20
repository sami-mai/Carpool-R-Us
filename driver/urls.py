<<<<<<< HEAD
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
=======
from django.conf.urls import url

>>>>>>> 2316c90bd16bfc1daeb4b3038f8d5bfc3ded17a1
from . import views as driver_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

<<<<<<< HEAD
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/logout/$', auth_views.logout, {"next_page": '/home'}),
    url(r'^home/', driver_views.home, name='home')
=======
    url(r'^home/', driver_views.home, name='home'),
>>>>>>> 2316c90bd16bfc1daeb4b3038f8d5bfc3ded17a1

]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
