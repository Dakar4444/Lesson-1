from django.core.management import BaseCommand
from shopapp.models import Product
from django.utils import lorem_ipsum
from random import randint, uniform



class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        name = lorem_ipsum.words(1, common=False).capitalize()
        description = lorem_ipsum.paragraphs(2, common=False)
        year = randint(2022, 2023)
        month = randint(1, 12)
        day = randint(1, 30)
        price = round(uniform(999.9, 99_999.99),2)
        quantity = randint(1, 100)
        
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            quantity = quantity,
            date_of_addition = f"{year}-{month}-{day}",
        )
        self.stdout.write(f"{product}")