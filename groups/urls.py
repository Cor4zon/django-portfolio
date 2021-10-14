
from django.urls import path, re_path
from django.conf.urls import url
from groups import views

urlpatterns = [
    url('albums', views.albums, name='albums'),
]