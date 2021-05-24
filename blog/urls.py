
from django.urls import path
from .views import index
from .views import blogList
urlpatterns = [
    path("", index, name="index",),
    path("blog-list/", blogList, name="blogList",)
]
