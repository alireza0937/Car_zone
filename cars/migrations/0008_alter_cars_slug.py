# Generated by Django 4.2.3 on 2023-07-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_cars_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=models.SlugField(default=1),
        ),
    ]