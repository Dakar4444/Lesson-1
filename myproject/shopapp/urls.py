from django.urls import path
from .views import get_order_by_user, upload_image


urlpatterns = [
    path('order/customer/<int:customer_pk>/', get_order_by_user, name='get_order_by_user'),
    path('upload/', upload_image, name='upload_image')
]