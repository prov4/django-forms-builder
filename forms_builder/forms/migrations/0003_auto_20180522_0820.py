# Generated by Django 2.0.4 on 2018-05-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20160418_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=1000, verbose_name='Slug'),
        ),
    ]
