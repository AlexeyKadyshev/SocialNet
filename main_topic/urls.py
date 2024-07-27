from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrance, name='entrance'),
    path('home/', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('friends/', views.friends, name='friends'),
    path('groups/', views.groups, name='groups'),
    path('profile/', views.profile, name='profile'),
    path('chat/', views.chat, name='chat'),
]
