from django.urls import path
from .views import CreateAccountView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('profile/', ProfileView.as_view(),
    name='profile'),
]
