from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^crud$', views.crudview, name='crudview'),
    url(r'^create$', views.create, name='create'),
    url(r'^index$', views.index, name='index'),
    url(r'^view$', views.view, name='view'),
    url(r'^update$', views.update, name='update'),
    url(r'^delete$', views.delete, name='delete'),
]