from django.db import models

class EnglishTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(language_taught='English')


class FrenchTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(language_taught='French')