from rest_framework import viewsets

from api.serializers import SongSerializer, AlbumSerializer, ArtistSerializer
from api.models import Album, Artist, Song


class SongViewSet(viewsets.ModelViewSet):
    """Viewset для работы с песнями."""

    queryset = Song.objects.select_related(
        'album',
        'album__artist',
    )
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """Viewset для работы с альбомами."""

    queryset = Album.objects.select_related(
        'artist'
    ).prefetch_related(
        'songs'
    )
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """Viewset для работы с исполнителями."""

    queryset = Artist.objects.prefetch_related('albums')
    serializer_class = ArtistSerializer
