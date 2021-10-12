from django.urls import path
from projects import views

# в каком это namespace
app_name = "projects"

urlpatterns = [
    path('', views.project_list),
    path('all_projects', views.all_projects),
    path('<int:pk>', views.project_details, name='project_details'),  # name of the path
]