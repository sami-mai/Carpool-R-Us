from django.conf.urls import url, include
from django.contrib.auth import views
# from . import views as driver_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^accounts/login', views.login, name="login"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.backends.hmac.urls')), -- for email confirmation
    url(r'^accounts/logout/$', views.logout, {"next_page": '/'}),
    # url(r'^tinymce/', include('tinymce.urls')), -- for smart editor

    # url('^$', views.home, name='home'),
    # url(r'^login/', views.login, name="login"),
    # url(r'^accounts/profile/(\d+)', views.user_profile, name="user_profile"),
    # url(r'^accounts/edit-profile/(\d+)', views.edit_profile, name='edit_profile'),
    # url(r'^accounts/upload-photo/', views.upload_photo, name='upload_photo'),
    # url(r'^post-comment/(/d+)', views.post_comment, name='post_comment'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^follow/(\d+)', views.follow, name="follow"),
    # url(r'^likes/(\d+)', views.like_image, name='like_image'),
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
