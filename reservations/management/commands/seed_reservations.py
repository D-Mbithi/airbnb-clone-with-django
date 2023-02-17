import random
from datetime import datetime, timedelta

from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed

from reservations import models as reservation_model
from rooms import models as room_model
from users import models as user_model

NAME = "Reservations"


class Command(BaseCommand):
    help = f"This command helps create {NAME} data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=2,
            help=f"How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        rooms = room_model.Room.objects.all()
        guests = user_model.CustomUser.objects.all()
        seeder = Seed.seeder()

        seeder.add_entity(
            reservation_model.Reservation,
            number,
            {
                "status": lambda x: random.choice(
                    ["pending", "confirmed", "cancelled"]
                ),
                "room": lambda x: random.choice(rooms),
                "guest": lambda x: random.choice(guests),
                "check_in": lambda x: datetime.now()
                + timedelta(days=random.randint(0, 5)),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(5, 25)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{NAME} created."))
