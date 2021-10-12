from django.shortcuts import render
from projects.models import Project


# Create your views here.
def all_projects(request):
    # query to DB to return all project objects
    projects = Project.objects.all()
    return render(request, "projects/all_projects.html", context={'projects': projects})


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "projects/details.html", {'project': project})


def project_list(request):
    return render(request, "index.html")

