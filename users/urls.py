from django.urls import path, re_path
from django.conf.urls import url
from users import views


urlpatterns = [
    url('index', views.index, name='index'),
]
