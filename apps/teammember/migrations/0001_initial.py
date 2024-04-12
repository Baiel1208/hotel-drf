# Generated by Django 4.2 on 2024-04-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('photo', models.ImageField(upload_to='team_photos/', verbose_name='Фото')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Коллектив',
                'verbose_name_plural': 'Коллектив',
            },
        ),
    ]
