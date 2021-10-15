# blog/urls.py

from django.urls import path, re_path, include
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    path("view_blog/<int:pk>/", views.view_blog, name="view_blog"),
    path("see_request", views.see_request, name="see_request"),
    path("user_info", views.user_info, name="user_info"),
    path("private_place", views.private_place, name="private_place"),
    path("staff_place", views.staff_place, name="staff_place"),
    path("add_messages", views.add_messages, name="add_messages"),
]
