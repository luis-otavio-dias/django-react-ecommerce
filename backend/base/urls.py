from django.urls import path
from base import views

urlpatterns = [
    path("products/", views.getProducts, name="products"),
    path("products/<str:pk>", views.getProduct, name="product"),
]
