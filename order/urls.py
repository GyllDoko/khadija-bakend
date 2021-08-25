from django.urls import path
from order import views
urlpatterns = [
    path("save_order/", views.save_order),    
]
