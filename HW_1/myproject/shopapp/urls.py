from django.urls import path
from . import views


urlpatterns = [
    path('order/customer/<int:customer_pk>/', views.get_order_by_user, name='get_order_by_user'),
]