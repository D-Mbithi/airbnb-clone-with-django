from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model
    """

    # Gender choices
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = ((GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Femal'), (GENDER_OTHER, 'Other'))

    # Language choices
    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, 'English'), (LANGUAGE_KOREAN, 'Korean'))

    # Currency choices
    CURRENCY_USD = 'USD'
    CURRENCY_KOREAN = 'KRW'

    CURRENCY_CHOICES = ((CURRENCY_KOREAN, 'Korean'),(CURRENCY_USD, 'USD'))


    avatar      = models.ImageField(blank=True)
    bio         = models.TextField(blank=True)
    gender      = models.CharField(choices=GENDER_CHOICES, max_length=10)
    birth_date  = models.DateField(null=True, blank=True)
    language    = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency    = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost   = models.BooleanField(default=False)
