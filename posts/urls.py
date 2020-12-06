"""Posts urls."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(route='posts/<int:pk>/',
         view=views.DetailPostView.as_view(),
         name='detail'),

    path(
        route='',
        view=views.ListPostView.as_view(),
        name='feed'),


    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'),
]
