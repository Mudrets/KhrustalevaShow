# Generated by Django 3.0.8 on 2020-08-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additions', '0002_auto_20200724_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='addition',
            name='slug',
            field=models.SlugField(default=1, verbose_name='ссылка на дополнение'),
        ),
    ]
