# Generated by Django 5.1.7 on 2025-03-21 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_categories', '0019_remove_hobbycategory_members'),
        ('users', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='current_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_members', to='hobby_categories.hobbycategory', verbose_name='Текущая категория'),
        ),
    ]
