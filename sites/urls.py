from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration$', views.userRegistration, name='registration'),
    url(r'^login$', views.userLogIn, name='login'),
    url(r'^dashboard$', views.dashBoard, name='dashboard'),
    url(r'^logout$', views.userLogOut, name='logout'),
]