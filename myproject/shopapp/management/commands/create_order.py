from django.core.management import BaseCommand
from shopapp.models import User, Product, Order
from random import randint, choice, choices, randrange



class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        customers = choice(User.objects.all())
        products = choices(Product.objects.all(), k=randrange(1,3) )
        total_price = 0
        
        year = randint(2023,2024)
        month = randint(1, 2)
        day = randint(1, 25)

        order = Order.objects.create(        
            customer = customers,
            total_price = total_price,
            date_order =f"{year}-{month}-{day}" ,
        )
        order.products.set(products)
        order.total_price = sum([item.price for item in products])
        order.save()

        self.stdout.write(f"{order}")
