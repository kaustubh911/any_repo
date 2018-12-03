from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'student_info', views.studentfunc)
]