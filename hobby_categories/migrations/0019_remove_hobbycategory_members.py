# Generated by Django 5.1.7 on 2025-03-21 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_categories', '0018_hobbycategory_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbycategory',
            name='members',
        ),
    ]
