# Generated by Django 5.2.3 on 2025-07-13 11:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tadApp', '0007_alter_projectimage_image_alter_sponsor_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='image'),
        ),
    ]
