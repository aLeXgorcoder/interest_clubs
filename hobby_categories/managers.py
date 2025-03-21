from django.apps import apps
from django.db import models


class MusicCategoryManager(models.Manager):
    def get_queryset(self):  # noqa
        """
        Возвращает пользователей, которые находятся в категории 'Музыка'.
        """
        music_categories = apps.get_model('hobby_categories', 'HobbyCategory').objects.filter(title='Музыка')
        if music_categories.exists():
            return apps.get_model('users', 'CustomUser').objects.filter(
                current_category__in=music_categories)
        return apps.get_model('users', 'CustomUser').objects.none()


class MovieCategoryManager(models.Manager):
    def get_queryset(self):  # noqa
        """
        Возвращает пользователей, которые находятся в категории 'Кино'.
        """
        movie_categories = apps.get_model('hobby_categories', 'HobbyCategory').objects.filter(title='Кино')
        if movie_categories.exists():
            return apps.get_model('users', 'CustomUser').objects.filter(
                current_category__in=movie_categories)
        return apps.get_model('users', 'CustomUser').objects.none()
