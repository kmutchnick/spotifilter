from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FilterForm
from .models import FilterSubmission
from .spotify_processing import *

# Create your views here.
def index(request):
    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            # print(form)
            # s = FilterSubmission(
            #     duration_ms_val=form.cleaned_data['duration_ms_val'],
            #     duration_ms_atleast=form.cleaned_data['duration_ms_atleast'],
            #     key_val=form.cleaned_data['key_val'],
            #     mode_val=form.cleaned_data['mode_val'],
            #     time_signature_val=form.cleaned_data['time_signature_val'],
            #     acousticness_val=form.cleaned_data['acousticness_val'],
            #     acousticness_atleast=form.cleaned_data['acousticness_atleast'],
            #     danceability_val=form.cleaned_data['danceability_val'],
            #     danceability_atleast=form.cleaned_data['danceability_atleast'],
            #     energy_val=form.cleaned_data['energy_val'],
            #     energy_atleast=form.cleaned_data['energy_atleast'],
            #     instrumentalness_val=form.cleaned_data['instrumentalness_val'],
            #     instrumentalness_atleast=form.cleaned_data['instrumentalness_atleast'],
            #     liveness_val=form.cleaned_data['liveness_val'],
            #     liveness_atleast=form.cleaned_data['liveness_atleast'],
            #     loudness_val=form.cleaned_data['loudness_val'],
            #     loudness_atleast=form.cleaned_data['loudness_atleast'],
            #     speechiness_val=form.cleaned_data['speechiness_val'],
            #     speechiness_atleast=form.cleaned_data['speechiness_atleast'],
            #     valence_val=form.cleaned_data['valence_val'],
            #     valence_atleast=form.cleaned_data['valence_atleast'],
            #     tempo_val=form.cleaned_data['tempo_val'],
            #     tempo_atleast=form.cleaned_data['tempo_atleast'],
            # )
            # print(s)
            # submission = s.save()
            # print(submission)
            submission = form.save()
            return HttpResponseRedirect('/results/%i' %submission.id)

    context = {'form':form}
    return render(request, 'main/index.html', context)

def results(request, id):
    playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
    submission = FilterSubmission.objects.get(id=id)
    active_attributes = {}
    fields = [f.get_attname() for f in submission._meta.fields]
    for field in fields:
        value = getattr(submission, field)
        if value:
            active_attributes[field] = value
    filtered_tracks = process(playlist_id, active_attributes)

    context = {'submission':submission, 'active_attributes':active_attributes, 'filtered_tracks':filtered_tracks}
    return render(request, 'main/results.html', context)