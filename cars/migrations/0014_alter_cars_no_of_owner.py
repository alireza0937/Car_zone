# Generated by Django 4.2.3 on 2023-07-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_cars_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='no_of_owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
