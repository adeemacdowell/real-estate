from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import RedirectView

from authweb.config.views import view_page


admin.autodiscover()


urlpatterns = [
    url(r'^(?P<url>[-\w]+)$', view_page, name='view_page'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'assets/favicon.ico')),
]