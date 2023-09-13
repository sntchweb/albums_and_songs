from rest_framework import serializers

from api.models import Artist, Album, Song


MIN_VALUE = 1
MAX_VALUE = 32767


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор песни."""

    album = serializers.CharField(source='album.name')
    artist = serializers.CharField(source='album.artist.name')
    song = serializers.CharField(source='name')

    class Meta:
        model = Song
        fields = ('song', 'album', 'artist')


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор альбома."""

    songs = SongSerializer(many=True)
    artist = serializers.CharField(source='artist.name')
    relese_year = serializers.IntegerField(
        min_value=MIN_VALUE, max_value=MAX_VALUE
    )

    class Meta:
        model = Album
        fields = ('name', 'artist', 'relese_year', 'songs')


class ArtistSerializer(serializers.ModelSerializer):
    """Сериализатор исполнителя."""

    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('name', 'albums')
