from django.shortcuts import render, HttpResponse
from groups.models import AlbumCard

# Create your views here.
def index(request):
    return render(request, 'base.html')


def albums(request):
    albums = AlbumCard.objects.all()
    # print(albums)
    return render(request, 'groups/albums.html', context={'albums': albums})


def albumInfo(request, pk):
    album = AlbumCard.objects.get(pk=pk)
    return render(request, 'groups/albumInfo.html', context={'album': album})