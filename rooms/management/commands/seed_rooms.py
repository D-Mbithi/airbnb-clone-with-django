import random

from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed

from rooms import models as room_model
from users import models as user_model


class Command(BaseCommand):
    help = "This command creates rooms "

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            help="How many rooms should be created",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = user_model.CustomUser.objects.all()
        room_types = room_model.RoomType.objects.all()
        all_ameninties = room_model.Amenity.objects.all()
        all_facilites = room_model.Facility.objects.all()
        all_rules = room_model.HouseRule.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            room_model.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(5, 20),
                "beds": lambda x: random.randint(1, 5),
                "bath": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "guest": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))

        for pk in created_clean:
            room = room_model.Room.objects.get(pk=pk)

            for i in range(3, random.randint(7, 18)):
                room_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",
                )
            for a in all_ameninties:
                if (random.randint(0, 15)) % 2 == 0:
                    room.amenities.add(a)

            for f in all_facilites:
                if (random.randint(0, 15)) % 2 == 0:
                    room.facilities.add(f)

            for r in all_rules:
                if (random.randint(0, 15)) % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS("Rooms created."))

        self.stdout.write(self.style.SUCCESS("Rooms created."))
