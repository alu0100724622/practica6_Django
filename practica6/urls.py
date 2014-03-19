from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica5.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^help', 'P6.views.help', name='help'),
    url(r'^home', 'P6.views.home', name='home'),
    url(r'^about', 'P6.views.about', name='about'),
)
