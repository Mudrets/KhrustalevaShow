# Generated by Django 3.0.8 on 2020-08-03 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
