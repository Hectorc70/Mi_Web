# Generated by Django 3.0.2 on 2021-02-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0004_auto_20210223_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
