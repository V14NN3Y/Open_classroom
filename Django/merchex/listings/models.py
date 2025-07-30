from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    class Type(models.TextChoices):
        Records = 'R'
        Clothing = 'C'
        Posters = 'P'
        Miscellaneous = 'M'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    description = models.fields.CharField(max_length=10000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=3)
    # like_new = models.fields.BooleanField(default=False)

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)