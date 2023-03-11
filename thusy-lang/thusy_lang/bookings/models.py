#from msilib.schema import Verb
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

class Teacher(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=75,
        unique=False,
        blank=False,
        null=False)
    middle_name = models.CharField(
        verbose_name='Middle Name', 
        max_length=75,
        unique=False,
        blank=True,
        null=True)
    last_name = models.CharField(
        verbose_name='Last Name', 
        max_length=75,
        unique=False,
        blank=False,
        null=False)
    language_taught = models.CharField(
        verbose_name='Language Taught',
        max_length=75,
        unique=False,
        blank=False,
        null=False)


class Location(models.Model):
    name = models.CharField(
        verbose_name='Location Name',
        max_length=255,
        unique=False,
        blank=False,
        null=False)
    address = models.CharField(
        verbose_name='Address',
        max_length=255)
    max_pupils = models.IntegerField(
        verbose_name='Max Pupils')

class Lesson(models.Model):
    name = models.CharField(
        verbose_name='Lesson Name',
        max_length=255)
    price_per_hour=MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency='EUR',
        null=False,
        validators=[
            MinMoneyValidator(
                {'EUR': 25, 'GBP': 20}),
            MaxMoneyValidator(
                {'EUR': 2500, 'GBP': 2000})
        ]
     )