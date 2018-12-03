from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^django_web_page$', views.helloDjango),
    url(r'homePage', views.homePage, name='myHome')
]