# Generated by Django 3.0.8 on 2020-08-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_auto_20200803_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='ссылка на героя'),
        ),
    ]
