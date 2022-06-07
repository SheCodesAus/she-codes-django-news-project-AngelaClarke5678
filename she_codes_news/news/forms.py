from secrets import choice
from unicodedata import category
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Category


choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','pub_date','content','story_img', 'category']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            # 'category':forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            }

# class EditStory(ModelForm):
