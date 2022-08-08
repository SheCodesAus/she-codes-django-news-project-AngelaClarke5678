from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, default="uncategorised")
    
    def __str__(self):
        return self.name


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    story_img = models.CharField(max_length=500, default="https://i.picsum.photos/id/1060/5598/3732.jpg?hmac=31kU0jp5ejnPTdEt-8tAXU5sE-buU-y1W1qk_BsiUC8")
    category = models.CharField(max_length=255, default="uncategorised")

class Author(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    author = user.name

    def get_absolute_url(self):
        return reverse("author", kwargs={'pk':self.pk})

    def __str__(self):
        return self.author.username