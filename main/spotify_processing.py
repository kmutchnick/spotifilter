import requests
import base64
from .secrets import *
import json

def generate_token():
    # Authorization setup
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = "{}:{}".format(clientId, clientSecret)
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    # Setup and execute call to generate and return token
    headers['Authorization'] = "Basic {}".format(base64Message)
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']

    return token


def extract_tracks_from_playlist(token, playlist_id):
    # Function to get tracks from the playlist
    # GET https://api.spotify.com/v1/playlists/{playlist_id}/tracks
    # Check parameters, limit max 100, default 100 to return
    # Returns an array of track objects, which contains id and uri
    playlist_track_ids_dict = {}
    url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
    )
    response_json = response.json()

    if response_json.get('items'):
        for item in response_json['items']:
            playlist_track_ids_dict[item['track']['id']] = [item['track']['name'],
                                                            item['track']['artists'][0]['name'],
                                                            item['track']['external_urls']['spotify'],
                                                            item['track']['preview_url']]

    return playlist_track_ids_dict

def filter_tracks(token, track_id_dict, active_attributes):
    # Function to check if tracks meet criteria, return tracks that meet criteria
    # GET https://api.spotify.com/v1/audio-features?ids=TrackID1,TrackID2,TrackIDN…
    track_ids = track_id_dict.keys()
    url = "https://api.spotify.com/v1/audio-features?ids={}".format(",".join(track_ids))
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
    )
    print(response)
    response_json = response.json()
    features = response_json['audio_features']

    for attribute, value in active_attributes.items():
        if "_atleast" in attribute or "id" in attribute:
            continue
        else:
            formatted_attribute = format_attribute(attribute)
            for track in features:
                if formatted_attribute is "key" or formatted_attribute is "mode" or formatted_attribute is "time_signature":
                    if track[formatted_attribute] != value and track_id_dict.get(track['id']):
                        del track_id_dict[track['id']]
                else:
                    if (track[formatted_attribute] < value) is bool(active_attributes.get(formatted_attribute+"_atleast")) and track_id_dict.get(track['id']):
                        del track_id_dict[track['id']]

    return track_id_dict

def format_attribute(attribute):
    s = attribute.replace('_val','')
    return s

def process(playlist_id, active_attributes):
    filtered_tracks = {}
    token = generate_token()
    track_ids = extract_tracks_from_playlist(token, playlist_id)
    if bool(track_ids):
        filtered_tracks = filter_tracks(token, track_ids, active_attributes)
    return filtered_tracks

