from datetime import datetime, timedelta
from flask import Flask, redirect, request, jsonify, session, render_template
import requests
import urllib.parse
import json

CLIENT_ID = "df434140a3534ccd96cd05cc1c0fde82"
CLIENT_SECRET = "647ad0bebb6042b48c0f82aaf02be283"

app = Flask(__name__)
app.secret_key = '36zRc2jMKTWGM1Fg6xi1g6fququBL5vX'

REDIRECT_URI ='http://localhost:5000/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

ids = []

# root
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-top-read'

    params ={
        'client_id' :CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri' : REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code' : request.args['code'],
            'grant_type' : 'authorization_code',
            'redirect_uri' : REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret' : CLIENT_SECRET
        }
        response = requests.post(TOKEN_URL, data=req_body)      
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] =  datetime.now().timestamp() + token_info['expires_in']
        # return redirect('/results')    
        return redirect('/top') 

@app.route('/results')
def get_playlist():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    headers = {
        'Authorization' : f"Bearer {session['access_token']}"
    }

    response = requests.get(API_BASE_URL + 'me/results', headers=headers)
    playlists = response.json()

    return jsonify(playlists)

@app.route('/top')
def get_top_tracks():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    headers = {
        'Authorization' : f"Bearer {session['access_token']}"
    }

    response = requests.get("https://api.spotify.com/v1/me/top/tracks?time_range=medium_term&limit=10", headers=headers)
    
    songs = json.loads(response.content)["items"]
    ids = []
    for idx, song in enumerate(songs):
        ids.append(song["id"])
    
    id_string = f"{ids[0]},{ids[1]},{ids[2]},{ids[3]},{ids[4]},{ids[5]},{ids[6]},{ids[7]},{ids[8]},{ids[9]}"
    song_response = requests.get("https://api.spotify.com/v1/audio-features?ids=" + id_string, headers=headers)
    song_data = song_response.json()

    traits = {'acousticness': 0.0, 
              'danceability': 0.0, 
              'energy': 0.0, 
              'instrumentalness': 0.0, 
              'liveness': 0.0, 
              'loudness': 0.0,
              'speechiness': 0.0, 
              'valence': 0.0
            }
    
    for idx, feature in enumerate(song_data['audio_features']):
        for key in traits:
            traits[key] += abs(feature[key])
    for key in traits:
        traits[key] = traits[key] / 10
    traits['loudness'] = (1 - (traits['loudness']) / 60)*0.75 #nerfed
    personality = max(traits, key=traits.get)
    
    match personality:
        case 'acousticness':
            return render_template("results.html", image_path="")
        case 'danceability':
            return render_template("results.html", image_path="")
        case 'energy':
            return render_template("results.html", image_path="")
        case 'instrumentalness':
            return render_template("results.html", image_path="")
        case 'liveness':
            return render_template("results.html", image_path="")
        case 'loudness':
            return render_template("results.html", image_path="")
        case 'speechiness':
            return render_template("results.html", image_path="")
        case 'valence':
            return render_template("results.html", image_path="")

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type' : 'refresh_token',
            'refresh_token' : session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret' : CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json
        session['access_token'] = new_token_info['access_token']
        session['expires_at'] =  datetime.now().timestamp() + new_token_info['expires_in']
        return redirect('/results')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)