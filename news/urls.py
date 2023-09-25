from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home-page"),
    path("news/<int:id>/", views.news_details, name="news-details-page"),
    path("categories/", views.categories_form, name="categories-form"),
    path("news/", views.news_form, name="news-form"),
]