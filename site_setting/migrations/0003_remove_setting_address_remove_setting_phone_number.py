# Generated by Django 4.2.3 on 2023-07-15 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_alter_setting_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='address',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='phone_number',
        ),
    ]
