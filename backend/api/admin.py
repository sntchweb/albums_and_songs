from django.contrib import admin

from api.models import Album, Artist, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ('name', 'artist', 'relese_year')
    list_display = ('name', 'artist', 'relese_year')
    list_filter = ('artist', 'relese_year')
    search_fields = ('name', )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('name', 'album')
    list_display = ('name', 'album')
    list_filter = ('album', 'album__artist__name')
    search_fields = ('name', )
