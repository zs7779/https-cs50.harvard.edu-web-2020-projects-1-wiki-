from django.urls import path

from . import views


app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<slug:title>", views.wiki, name="wiki"),
    path("new/", views.new, name="new"),
    path("new/<slug:title>", views.new, name="new"),
    path("search/", views.search, name="search")
]
