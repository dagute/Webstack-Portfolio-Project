from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    twitter_link = models.URLField(max_length=255)
    github_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
