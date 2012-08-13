from django.conf.urls.defaults import *
from django.contrib import admin
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # gae
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    # django admin and login
    (r'^admin/', include(admin.site.urls)),
)
