from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('feed/create/', views.create_post, name='create-post'),
    path('feed/like/<int:pk>/', views.like_post, name='like-post'),
    path('feed/comment/<int:pk>/', views.add_comment, name='add-comment'),
]