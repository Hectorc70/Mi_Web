# Generated by Django 3.0.2 on 2021-03-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0011_auto_20210322_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code_link',
            field=models.CharField(default='', max_length=500, verbose_name='link codigo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.CharField(default='', max_length=500, verbose_name='link demo'),
            preserve_default=False,
        ),
    ]
