from django.urls import path
from order import views
urlpatterns = [
    path("save_order/", views.save_order),
    path("get_order_products/<str:order>/", views.get_order_products),
    path("get_order/<int:user>/", views.get_order),
]
