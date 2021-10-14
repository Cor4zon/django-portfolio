from django.urls import path, re_path, include
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url('index', views.index, name='index'),
]
