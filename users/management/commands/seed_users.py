from django.core.management.base import BaseCommand
from django_seed import Seed

from users.models import CustomUser


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
        seeder = Seed.seeder()
        seeder.add_entity(
            CustomUser,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Users created."))
