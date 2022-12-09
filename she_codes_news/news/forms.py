from secrets import choice
from unicodedata import category
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.utils import timezone,dateformat


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "pub_date", "content", "image", "category"]
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")