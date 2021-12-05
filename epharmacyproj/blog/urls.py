from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogPost"),
    path("popularpost/<int:id>", views.popularpost, name="popularpost"),
]