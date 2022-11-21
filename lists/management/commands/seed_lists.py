import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_model
from users import models as user_model
from rooms import models as room_model


NAME = "Lists"

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
        users = user_model.User.objects.all()
        seeder = Seed.seeder()

        seeder.add_entity(
            list_model.List,
            number, 
            {
                "user": lambda x: random.choice(users),
            }
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_obj = list_model.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0,5):random.randint(6,30)]
            list_obj.rooms.add(*to_add)                


        self.stdout.write(self.style.SUCCESS(f"{NAME} created."))
