# Generated by Django 5.1.7 on 2025-03-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_categories', '0004_alter_hobbycategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbycategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
