#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
import json
from io import StringIO
import time
import spotify_token as st

query = ''
currentSong = ''
USER = os.environ.get('SP_DC')
PW = os.environ.get('SP_KEY')
TOKEN = ''

def get_token():
    """ Get an OAuth token for Spotify """
    global TOKEN
    try:
        data = st.start_session(USER,PW)
        TOKEN = data[0]
        EXPIRATION_DATE = data[1]
    except:
        quit('Unable to get OAuth Token :-( -- Check you have set your Spotify username and password correctly.')


def song_data():
    """ Query the Spotify API for currently playing song """
    global query
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + TOKEN,
    }

    try:
        response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
        json_data = json.loads(response.text)
        ARTIST = json_data["item"]["artists"][0]["name"]
        SONG = json_data["item"]["name"]
        query = SONG + " " + ARTIST + " +lyrics"
        return('Artist: %s\nSong: %s' % (ARTIST, SONG))
    except:
        #print('JSON Response Error.')  # TODO handle this better
        get_token()  # Hacky, but fair to assume if API is not responding it could be due to an expired token
        # print(response.content)
        return(' ')


def get_Song_Lyrics(query):
    """ Download lyrics for current song """
    headers_Get = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    lyric_text = '\n'
    s = requests.Session()
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers_Get)
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser").find_all("span", {"jsname": "YS01Ge"})
    # print(soup)
    for link in soup:
        # print(link)
        lyric_text += (link.text + '\n')
    return lyric_text


def main():
    """ Main loop """
    get_token()  # Get an oAuth token
    currentSong = ''

    while True:  # Main loop
        if song_data() != currentSong:  # Check if the song has changed
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            print(song_data())  # Print song info
            lyrics = get_Song_Lyrics(query)
            if len(lyrics) < 2:
                print('\nNo lyrics found 🎸')
            else:
                print(lyrics)
            currentSong = song_data()
        time.sleep(1)  # Delay between checking the Spotify API again


if __name__ == '__main__':
    """ Boilerplate """
    try:
        main()
    except KeyboardInterrupt:
        print('Quitting..')
        try:
            quit()
        except SystemExit:
            quit()
