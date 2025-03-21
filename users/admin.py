from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'gender', 'current_category')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Редактировать информацию о пользователе'
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Выберите пользователя для редактирования'
        return super().changelist_view(request, extra_context=extra_context)

    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'email', 'age', 'gender')
        }),
        ('Категория хобби', {
            'fields': ('current_category',)
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_header = 'Интерфейс управления приложением "Клубы по интересам"'
admin.site.site_title = 'Администрирование приложения "Клубы по интересам"'
