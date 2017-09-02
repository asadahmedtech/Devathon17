from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
app_name = 'problempost'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentcouncil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^redirect', views.index, name="index"),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^statuschange/$', views.statuschange, name='statuschange'),
    url(r'^new/$', views.new_form, name='new_form'),
    url(r'^newpost/$', views.post_new, name = 'post_new'),
    url(r'^show/$', views.post_get, name = 'post_get'),
    url(r'^showtocouncil/$', views.councilMemComplaint, name = "councilMem_complaint")
        )
