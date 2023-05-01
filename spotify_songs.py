from dotenv import find_dotenv, load_dotenv
from os import environ as env
import base64
from requests import post, get
import json
import random
from song import *
from download_song import *

# ERR_PLAYLIST_MSG = "Error loading Playlist"

# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)

# client_id = env.get('CLIENT_ID')
# client_secret = env.get('CLIENT_SECRET')

# happy_playlist = "4AnAUkQNrLKlJCInZGSXRO"
# sad_playlist = "2tN9jIiiCBLCSAVuaVvgHX"
# angry_playlist = "3Qtb7W0YeJdar6w44Df28z"
# neutral_playlist = "37i9dQZF1EVHGWrwldPRtj"

# #refresh token for spotify

# def get_token():
#     auth_string = client_id + ":" + client_secret
#     test_string = 'test'
#     auth_bytes = auth_string.encode('utf-8')
#     auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

#     url = "https://accounts.spotify.com/api/token"

#     headers = {
#         "Authorization": "Basic " + auth_base64,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {"grant_type": "client_credentials"}
#     result = post(url, headers=headers, data=data)
#     json_result = json.loads(result.content)
#     token = json_result["access_token"]
#     return token

# def get_auth_header(token):
#     return {"Authorization" : "Bearer " + token}

# def get_playlist(token, playlist_id):
#     url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items%28track%28name%2C+artists.name%2C+album.images%29%29"
#     headers = get_auth_header(token)
#     result = get(url, headers=headers)
#     json_result = json.loads(result.content)
#     songs = []
#     if "items" not in json_result:
#         return ERR_PLAYLIST_MSG
#     for song_info in json_result["items"]:
#         song = Song(song_info['track']['name'], song_info['track']['artists'][0]['name'], song_info['track']['album']['images'][0]['url'])
#         songs.append(song)
#     return songs

# token = get_token()

# happy_songs = get_playlist(token, happy_playlist)
# sad_songs = get_playlist(token, sad_playlist)
# angry_songs = get_playlist(token, angry_playlist)
# neutral_songs = get_playlist(token, neutral_playlist)

# moods = [happy_songs, sad_songs, angry_songs, neutral_songs]


# def choose_mood(arr):
#     return moods[arr.index(max(arr))]

# def random_songs(arr):
#     return random.choices(choose_mood(arr), k=5)

# song1 = random_songs([1,2,4,3])[0]
# download_song(song1)




# # print(song.get_name())










