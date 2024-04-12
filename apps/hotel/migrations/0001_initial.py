# Generated by Django 4.2 on 2024-04-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('location', models.CharField(max_length=100, verbose_name='Местоположение')),
                ('image', models.ImageField(upload_to='hotel_images/', verbose_name='Фоновое изображение')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
    ]
