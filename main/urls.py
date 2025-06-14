from django.urls import path
from .views import (
    home, detail, posts, create_post, latest_posts,
    search_result,edit_post,delete_post)

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),
    path('post/edit/<slug:slug>/', edit_post, name='edit_post'),
    path('post/delete/<slug:slug>/', delete_post, name='delete_post')
]