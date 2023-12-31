# Generated by Django 4.2.3 on 2023-07-26 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='is_response',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
