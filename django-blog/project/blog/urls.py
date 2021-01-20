from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    CreatePostView,
                    PostUpdateView,
                    PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/new/', CreatePostView.as_view(), name='blog-create'),
    path('about/', views.about, name="blog-about"),
]