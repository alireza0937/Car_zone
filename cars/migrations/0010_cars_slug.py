# Generated by Django 4.2.3 on 2023-07-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_cars_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]