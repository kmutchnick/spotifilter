from django.forms import ModelForm
from .models import FilterSubmission
from django.forms.widgets import TextInput, Select

COMPARE_CHOICES = [
    (True, '≥'),
    (False, '<')
]

class FilterForm(ModelForm):
    class Meta:
        model = FilterSubmission
        fields = [
            'duration_ms_val',
            'duration_ms_atleast',
            'key_val',
            'mode_val',
            'time_signature_val',
            'acousticness_val',
            'acousticness_atleast',
            'danceability_val',
            'danceability_atleast',
            'energy_val',
            'energy_atleast',
            'instrumentalness_val',
            'instrumentalness_atleast',
            'liveness_val',
            'liveness_atleast',
            'loudness_val',
            'loudness_atleast',
            'speechiness_val',
            'speechiness_atleast',
            'valence_val',
            'valence_atleast',
            'tempo_val',
            'tempo_atleast',
        ]
        widgets = {
            # 'duration_ms_val' : RangeInput(attrs={'max': 300000, 'min': 0, 'step': 1000}),
            'duration_ms_val': TextInput(attrs={'type': 'range', 'max': 300000, 'min': 0, 'step': 1000}),
            'duration_ms_atleast': Select(choices=COMPARE_CHOICES)
        }