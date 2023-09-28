# example/urls.py
from django.urls import path

from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]