from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello-world.txt', views.text_file),
    path('image.jpg', views.image_file),
    path('style.css', views.css)
]
