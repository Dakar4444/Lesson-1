from django.core.management import BaseCommand
from shopapp.models import User
from random import randint



class Command(BaseCommand):
    help = "Create user"

    def add_arguments(self, parser):
        parser.add_argument("name")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        adres = randint(1,50)
        year = randint(2022, 2023)
        month = randint(1, 12)
        day = randint(1, 30)
        numb = randint(1_000_000, 9_999_999)
        user = User.objects.create(
            name = name,
            email = f"{name}_{year}@mail.ru",
            phone_number = f"37529{numb}",
            adress = f"{name} Street, h.{adres}",
            date_of_registration = f"{year}-{month}-{day}",
        )
        self.stdout.write(f"{user}")
