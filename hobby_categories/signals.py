from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode

from .models import HobbyCategory


@receiver(pre_save, sender=HobbyCategory)
def create_slug_for_category(sender, instance, **kwargs):
    if not instance.slug:
        slug = unidecode(instance.title)
        slug = slugify(slug)
        instance.slug = slug
