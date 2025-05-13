from django.urls import path
from . import views

# /product means url
# /products/new

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('old',views.old)
]