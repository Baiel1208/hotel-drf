# Generated by Django 4.2 on 2024-04-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammember', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='team_photos/', verbose_name='Фото'),
        ),
    ]
