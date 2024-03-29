from django.shortcuts import render, get_object_or_404, redirect
from shopapp.models import Order, User, Product
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
import datetime


# Create your views here.

def get_order_by_user(request, customer_pk):
    customer = get_object_or_404(User, pk=customer_pk)
    week_date = datetime.datetime.today() - datetime.timedelta(days=7)
    month_date = datetime.datetime.today() - datetime.timedelta(days=30)
    year_date = datetime.datetime.today() - datetime.timedelta(days=365)

    orders_week = Order.objects.filter(customer=customer, date_order__gte=week_date)
    orders_month = Order.objects.filter(customer=customer, date_order__gte=month_date)
    orders_year = Order.objects.filter(customer=customer, date_order__gte=year_date)
    
    # Я ЕЩЁ НЕ РАЗОБРАЛСЯ | СЛЕДУЮЩИМ КОМИТОМ СДЕЛАЮ | ОБЕЩАЮ
    '''
    orders_w = set()
    orders_m = set()
    orders_y = set()

    orders_week = Product.objects.filter(order__customer=customer, order__date_order__gte=week_date).distinct()
    orders_month = Product.objects.filter(order__customer=customer, order__date_order__gte=month_date).distinct()
    orders_year = Product.objects.filter(order__customer=customer, order__date_order__gte=year_date).distinct()
    
    orders_w.add(orders_week)
    orders_m.add(orders_month)
    orders_y.add(orders_year)

    print(orders_month)
    '''
    return render(request, "shopapp/customer_order.html", {"orders_week": orders_week, "orders_month": orders_month, "orders_year": orders_year, "customer": customer})


def upload_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ProductForm()
    return render(request, 'shopapp/upload_image.html', {'form':form})
