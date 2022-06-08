from secrets import choice
from unicodedata import category
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Category

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
        fields = ['title','pub_date','content','story_img', 'category']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }