from django.urls import path
from .views import home, profile, RegisterView, delete_user

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('delete/', delete_user, name='delete_user')
]
