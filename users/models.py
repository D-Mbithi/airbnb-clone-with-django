from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Custom user model."""

    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Gender choices
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Femal"),
        (GENDER_OTHER, "Other"),
    )

    # Language choices
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (
            LANGUAGE_ENGLISH,
            "English",
        ),
        (LANGUAGE_KOREAN, "Korean"),
    )

    # Currency choices
    CURRENCY_USD = "USD"
    CURRENCY_KOREAN = "KRW"

    CURRENCY_CHOICES = (
        (CURRENCY_KOREAN, "Korean"),
        (CURRENCY_USD, "USD"),
    )

    avatar = models.ImageField(upload_to="avatar", blank=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
        default=LANGUAGE_ENGLISH,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
        default=CURRENCY_USD,
    )
    super_host = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".title()
        return full_name
