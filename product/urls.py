from django.urls import path
from product import views

urlpatterns = [
    path("categories/", views.get_categories),
    path("products/<str:category>/", views.get_products),
    path("images/<str:product>/", views.get_images),
    path("descriptions/<str:product>/", views.get_descriptions),
]
