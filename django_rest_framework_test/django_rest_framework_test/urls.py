# coding: utf-8

from django.urls import path, include
from django.contrib import admin

from blog.urls import router as blog_router

urlpatterns = [
    path(r"admin/", admin.site.urls),
    # blog.urlsをincludeする
    path(r"api/", include(blog_router.urls)),
]
