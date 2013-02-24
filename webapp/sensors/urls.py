from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',     'sensors.views.test'),
    (r'^update$','sensors.views.update'),
)
