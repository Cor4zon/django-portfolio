from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'base.html')


def albums(request):
    return render(request, 'groups/albums.html')
