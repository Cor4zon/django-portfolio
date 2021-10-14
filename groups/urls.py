
from django.urls import path, re_path
from django.conf.urls import url
from groups import views

app_name = 'groups'

urlpatterns = [
    url('albums', views.albums, name='albums'),
    path('albumInfo/<int:pk>', views.albumInfo, name='albumInfo'),
]