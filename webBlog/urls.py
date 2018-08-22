from django.conf.urls import url, include
from . import views


urlpatterns = [
url('band', views.band, name='band'),
url('tour', views.tour, name='tour'),
url('contact', views.contact, name='contact'),
url('', views.index, name='index'),
]

