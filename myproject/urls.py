from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from myproject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
