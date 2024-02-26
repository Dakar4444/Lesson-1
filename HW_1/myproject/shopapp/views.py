from django.shortcuts import render, get_object_or_404
from shopapp.models import Order, User, Product
import datetime

# Create your views here.

def get_order_by_user(request, customer_pk):
    customer = get_object_or_404(User, pk=customer_pk)
    week_date = datetime.datetime.today() - datetime.timedelta(days=7)
    month_date = datetime.datetime.today() - datetime.timedelta(days=30)
    year_date = datetime.datetime.today() - datetime.timedelta(days=365)
    orders_week = Order.objects.filter(customer=customer, date_order__gte=week_date).all()
    orders_month = Order.objects.filter(customer=customer, date_order__gte=month_date).all()
    orders_year = Order.objects.filter(customer=customer, date_order__gte=year_date).all()
    return render(request, "shopapp/customer_order.html", {"orders_week": orders_week, "orders_month": orders_month, "orders_year": orders_year, "customer": customer})