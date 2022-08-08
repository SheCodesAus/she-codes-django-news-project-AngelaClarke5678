import imp
from django.views import generic
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Category, NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import SlugField

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4] # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by
        context['all_stories'] = NewsStory.objects.all()
        return context


class AuthorsListView(generic.ListView):
    form_class = StoryForm
    context_object_name = 'author_list'
    template_name = 'news/author.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(AuthorsListView, self).get_context_data(**kwargs)
        context['author'] = NewsStory.objects.all()
        return context

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return NewsStory.objects.filter(author = author_id,)

class CategoryListView(generic.ListView):
    models = Category
    context_object_name = 'category_list'
    template_name = 'news/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class CategoryView(generic.DetailView):
    model= Category
    slug_field = 'name'

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(LoginRequiredMixin,generic.UpdateView):
    model = NewsStory
    context_object_name = 'storyForm'
    fields = ['title', 'content', 'category', 'story_img']
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteStoryView(LoginRequiredMixin,generic.DeleteView):
    model = NewsStory
    context_object_name = 'storyForm'
    fields = ['title', 'content', 'story_img']
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')




