# Generated by Django 4.2.3 on 2023-07-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
