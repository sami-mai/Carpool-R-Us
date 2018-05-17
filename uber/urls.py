"""uber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login', views.login, name="login"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^rider/', include('rider.urls')),
    # url(r'^driver/', include('driver.urls')),
    # url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/logout/$', views.logout, {"next_page": '/'}),
    # url(r'^tinymce/', include('tinymce.urls')),
]
