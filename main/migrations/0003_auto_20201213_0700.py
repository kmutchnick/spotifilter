# Generated by Django 3.1.1 on 2020-12-13 07:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201213_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtersubmission',
            name='acousticness_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='danceability_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='duration_ms_val',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='energy_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='instrumentalness_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='key_val',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(-1)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='liveness_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='loudness_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(-60)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='mode_val',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='speechiness_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='tempo_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='time_signature_val',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='filtersubmission',
            name='valence_val',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0)]),
        ),
    ]