# Generated by Django 4.2.3 on 2023-07-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
