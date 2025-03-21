from django.apps import AppConfig


class HobbyCategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hobby_categories'
    verbose_name = "Категории клубов"

    def ready(self):
        try:
            import hobby_categories.signals
        except ImportError:
            pass
