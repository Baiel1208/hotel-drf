# Generated by Django 4.2 on 2024-04-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/', verbose_name='Фоновое изображение'),
        ),
    ]
