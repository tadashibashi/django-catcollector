from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cats/", views.CatsList.as_view(), name="cats_index"),
    path("cats/<int:pk>/", views.CatsDetail.as_view(), name="cats_detail"),
    path("cats/create/", views.CatsCreate.as_view(), name="cats_create"),
    path("cats/<int:pk>/update/", views.CatsUpdate.as_view(), name="cats_update"),
    path("cats/<int:pk>/delete/", views.CatsDelete.as_view(), name="cats_delete"),
]
