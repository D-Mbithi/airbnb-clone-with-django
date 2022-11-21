import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users import models as user_model
from rooms import models as room_model


class Command(BaseCommand):
    help = "This command helps create user data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=2,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        rooms = room_model.Room.objects.all()
        users = user_model.User.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number, {
                # "review": seeder.faker.sentence(),
                "accuracy": lambda x: random.randint(1, 6),
                "cleanliness": lambda x: random.randint(1, 6),
                "communication": lambda x: random.randint(1, 6),
                "location": lambda x: random.randint(1, 6),
                "checkin": lambda x: random.randint(1, 6),
                "value": lambda x: random.randint(1, 6),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Reviews created."))
