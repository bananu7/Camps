from django.conf.urls import patterns, url
from camps import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'add/$', views.CreateView.as_view(), name='add'),
)
