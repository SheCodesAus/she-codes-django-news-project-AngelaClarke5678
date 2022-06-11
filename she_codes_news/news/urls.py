from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<int:pk>', views.AuthorsListView.as_view(), name = 'author'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='delete'),
    path('<int:pk>/edit', views.EditStoryView.as_view(), name='edit'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<str:slug>',views.CategoryView.as_view(), name='categorydetail'),
]
