# Generated by Django 5.1.7 on 2025-03-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_categories', '0011_alter_hobbycategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbycategory',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='category_covers/'),
        ),
    ]
