# Generated by Django 3.0.2 on 2021-03-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0008_auto_20210308_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture_head',
            field=models.CharField(max_length=500, verbose_name='Imagen'),
        ),
    ]
