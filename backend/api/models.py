from django.db import models


class Artist(models.Model):
    """Модель исполнителя."""

    name = models.CharField(
        max_length=100,
        verbose_name='Имя исполнителя',
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    """Модель альбома."""

    name = models.CharField(
        max_length=150,
        verbose_name='Название альбома',
        blank=True,
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
        related_name='albums',
    )
    relese_year = models.IntegerField(verbose_name='Год выпуска альбома')

    class Meta:
        ordering = ('artist', )
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        constraints = (
            models.UniqueConstraint(
                fields=('artist', 'name'),
                name='unique_album_by_artist',
            ),
        )

    def __str__(self):
        return self.name


class Song(models.Model):
    """Модель песни."""

    name = models.CharField(
        max_length=100,
        verbose_name='Название песни',
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Альбом',
        related_name='songs',
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        constraints = (
            models.UniqueConstraint(
                fields=('album', 'name'),
                name='unique_song_in_album',
            ),
        )

    def __str__(self):
        return self.name
