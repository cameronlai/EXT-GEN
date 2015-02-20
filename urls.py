from django.conf.urls import patterns, url

from EXT_GEN import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)
