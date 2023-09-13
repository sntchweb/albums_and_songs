from django.urls import include, path
from rest_framework import routers

from api.views import AlbumViewSet, ArtistViewSet, SongViewSet


app_name = 'api'
router = routers.DefaultRouter()

router.register(r'albums', AlbumViewSet, basename='albums')
router.register(r'artists', ArtistViewSet, basename='artists')
router.register(r'songs', SongViewSet, basename='songs')

urlpatterns = [
    path('api/', include(router.urls)),
]
