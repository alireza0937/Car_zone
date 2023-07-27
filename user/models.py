from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True)
    about_user = models.TextField(blank=True)
    email_activation_code = models.CharField(max_length=150)
    address = models.TextField(blank=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'Users'


