from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    banner = models.ImageField(upload_to='banner/')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Setting'
        db_table = 'Setting'


class Contact(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    google_plus_link = models.URLField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Contact'
        db_table = 'Contact'
