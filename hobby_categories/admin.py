from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import HobbyCategory


class HobbyCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'cover_preview')
    readonly_fields = ["cover_preview"]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Редактировать категорию'
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Выберите категорию для редактирования'
        return super().changelist_view(request, extra_context=extra_context)

    def cover_preview(self, obj):
        if obj.cover:
            return mark_safe(f'<img src="{obj.cover.url}" width="120" height="100" style="border-radius:5px;" />')
        return "Нет изображения"

    cover_preview.short_description = "Обложка"


admin.site.register(HobbyCategory, HobbyCategoryAdmin)

admin.site.site_header = 'Интерфейс управления приложением "Клубы по интересам"'
admin.site.site_title = 'Администрирование приложения "Клубы по интересам"'
