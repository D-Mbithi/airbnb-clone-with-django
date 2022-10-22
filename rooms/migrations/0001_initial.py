# Generated by Django 4.1.2 on 2022-10-22 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=140)),
                ("description", models.TextField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("city", models.CharField(max_length=80)),
                ("price", models.IntegerField()),
                ("address", models.CharField(max_length=140)),
                ("bedrooms", models.IntegerField()),
                ("beds", models.IntegerField()),
                ("bath", models.IntegerField()),
                ("guest", models.IntegerField()),
                ("checkin", models.TimeField()),
                ("checkout", models.TimeField()),
                ("instant_book", models.BooleanField(default=False)),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
