# Generated by Django 3.1.1 on 2020-12-13 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_ms_val', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('key_val', models.IntegerField(validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(-1)])),
                ('mode_val', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('time_signature_val', models.IntegerField(validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(3)])),
                ('acousticness_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('danceability_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('energy_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('instrumentalness_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('liveness_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('loudness_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(-60)])),
                ('speechiness_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('valence_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)])),
                ('tempo_val', models.DecimalField(decimal_places=20, max_digits=25, validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
