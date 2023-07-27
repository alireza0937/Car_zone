from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.last_name)

    class Meta:
        db_table = 'Team'
        verbose_name_plural = 'Team'
