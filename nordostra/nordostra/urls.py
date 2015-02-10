from django.conf.urls import patterns, include, url
from django.contrib import admin
from nordostra import views
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session/$', 'nordostra.views.home', name='home'),
    url(r'^session/(?P<session>\d{1,4})/$', 'nordostra.views.percent', name='percent'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

    
