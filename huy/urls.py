from django.conf.urls import patterns, include, url
from huy.views import hello , current_datetime,hours_ahead
from hamagua.views import addTarget,addTargetForm,result,showMyTargets
from login.views import index,register,login,logout
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'huy.views.home', name='home'),
    # url(r'^huy/', include('huy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^addTarget/$',addTarget),
	(r'^addTargetForm/$',addTargetForm),
	(r'^result/$',result),
	(r'^index/$',index),
	(r'^register/$',register),
	(r'^logout/$',logout),
	(r'^login/$',login),
	(r'^targets/$',showMyTargets),
   
)




