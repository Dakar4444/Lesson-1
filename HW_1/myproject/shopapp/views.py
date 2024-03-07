from django.shortcuts import render, get_object_or_404, redirect
from shopapp.models import Order, User, Product
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from datetime import datetime


# Create your views here.

def get_order_by_user(request, customer_pk):
    customer = get_object_or_404(User, pk=customer_pk)
    today = datetime.now()
    orders = Order.objects.filter(customer=customer)
    
    orders_w = set()
    orders_m = set()
    orders_y = set()
    # Без помощи Виталика не обошлось
    for order in orders:
        date_diff = (today - datetime.fromisoformat(str(order.date_order))).days
        if date_diff <= 7:
            for product in order.products.all():
              orders_w.add(product)
              orders_m.add(product)
              orders_y.add(product)
        elif date_diff <= 30:
            for product in order.products.all():
              orders_m.add(product)
              orders_y.add(product)
        elif date_diff <= 365:
            for product in order.products.all():
              orders_y.add(product)
        
    return render(request, "shopapp/customer_order.html", {"orders_week": orders_w, "orders_month": orders_m, "orders_year": orders_y, "customer": customer})



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
