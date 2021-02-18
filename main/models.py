from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class FilterSubmission(models.Model):
    duration_ms_val = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    duration_ms_atleast = models.BooleanField(default=True)

    key_val = models.IntegerField(validators=[MaxValueValidator(23), MinValueValidator(-1)], null=True, blank=True)

    mode_val = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)], null=True, blank=True)

    time_signature_val = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(3)], null=True, blank=True)

    acousticness_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    acousticness_atleast = models.BooleanField(default=True)

    danceability_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    danceability_atleast = models.BooleanField(default=True)

    energy_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    energy_atleast = models.BooleanField(default=True)

    instrumentalness_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    instrumentalness_atleast = models.BooleanField(default=True)

    liveness_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    liveness_atleast = models.BooleanField(default=True)

    loudness_val = models.DecimalField(max_digits=6, decimal_places=2, validators=[MaxValueValidator(0), MinValueValidator(-60)], null=True, blank=True)
    loudness_atleast = models.BooleanField(default=True)

    speechiness_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    speechiness_atleast = models.BooleanField(default=True)

    valence_val = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(1.0), MinValueValidator(0)], null=True, blank=True)
    valence_atleast = models.BooleanField(default=True)

    tempo_val = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(250), MinValueValidator(0)], null=True, blank=True)
    tempo_atleast = models.BooleanField(default=True)