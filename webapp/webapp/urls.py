from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to0

# Uncomment the next two lines to enable the admino:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',redirect_to, {'url': '/sensors/'}),
    # url(r'^webapp/', include('webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # url(r'^admin/', include(admin.site.urls)),
    (r'^sensors/', include('sensors.urls'))

)
