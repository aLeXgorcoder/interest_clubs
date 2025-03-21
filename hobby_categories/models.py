from django.db import models

from .managers import MusicCategoryManager, MovieCategoryManager


class HobbyCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название клуба')
    description = models.TextField(blank=False, verbose_name='Описание')
    cover = models.ImageField(upload_to='category_covers/', verbose_name='Обложка')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')

    objects = models.Manager()
    music = MusicCategoryManager()
    movie = MovieCategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
