# Generated by Django 3.0.2 on 2021-02-22 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='Proyecto',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='id_proyecto',
            new_name='id_project',
        ),
    ]
