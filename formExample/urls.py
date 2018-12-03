from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forms$', views.form_example, name='form'),
    url(r'^static$', views.static_view),
]