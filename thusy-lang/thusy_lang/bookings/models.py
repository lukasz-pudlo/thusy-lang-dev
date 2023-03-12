#from msilib.schema import Verb
from email.policy import default
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django.db.models.functions import Lower

class Lesson(models.Model):
    name = models.CharField(
        verbose_name='Lesson Name',
        max_length=255)
    price_per_hour=MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency='EUR',
        null=False,
        default=25,
        validators=[
            MinMoneyValidator(
                {'EUR': 25, 'GBP': 20}),
            MaxMoneyValidator(
                {'EUR': 2500, 'GBP': 2000})
        ]
     )

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
    lesson=models.ManyToManyField(
        Lesson,
        verbose_name='Lessons',
        related_name='lesson_teachers',
        related_query_name='lesson_teacher',
        blank=True)
    location=models.ManyToManyField(
        Location,
        verbose_name='Locations',
        related_name='location_teachers',
        related_query_name='location_teacher')
    
    class Meta:
        ordering=['last_name', 'middle_name', 'first_name']
        indexes=[models.Index(fields=['last_name']),
        models.Index(
            fields=['-last_name'],
            name='desc_last_name_idx'),
        models.Index(
            Lower('last_name').desc(),
            name='lower_last_name_idx'
            )
        ]
    def __str__(self):
        return self.model.first_name + ' ' + self.model.middle_name + ' ' + self.model.last_name