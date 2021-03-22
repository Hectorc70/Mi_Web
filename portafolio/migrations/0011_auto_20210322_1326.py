# Generated by Django 3.0.2 on 2021-03-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='link_cv',
            field=models.CharField(blank=True, max_length=500, verbose_name='Path CV'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.CharField(blank=True, max_length=500, verbose_name='Imagen de perfil'),
        ),
    ]
