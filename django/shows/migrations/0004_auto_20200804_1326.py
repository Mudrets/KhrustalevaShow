# Generated by Django 3.0.8 on 2020-08-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20200804_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='ссылка на шоу'),
        ),
    ]
