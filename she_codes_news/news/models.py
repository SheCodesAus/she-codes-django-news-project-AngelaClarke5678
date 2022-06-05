from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    # story_img = models.ImageField(upload_to='she_codes_news/news/static/news/images/',null=True, blank=True)
    story_img = models.CharField(max_length=500, default="paste  your ")

