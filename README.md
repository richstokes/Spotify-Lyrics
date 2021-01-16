# Intro
The script will get your currently playing song on Spotify and automatically grab the lyrics.  

&nbsp;

# Setup
## Install requirements
`pip3 install -r requirements.txt`

&nbsp;


## Get credentials

> To use this program, you will need to get the `SP_DC` and `SP_KEY` cookie values.   


To obtain the cookies (valid for 1 year):

1. Open a new Incognito window in Chrome (or another browser) at https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F
2. Open Developer Tools in your browser (might require developer menu to be enabled in some browsers)
3. Login to Spotify.
4. Search/Filter for get_access_token in Developer tools under Network.
5. Under cookies for the request save the values for `sp_dc` and `sp_key`.
6. Close the window without logging out (Otherwise the cookies are made invalid).

&nbsp;


# Run
Export your Spotify Username and PW as environment variables and then start the script.  e.g.  

```
export SP_DC="abcxyz"
export SP_KEY="abcxyz"
python3 spotifylyrics.py
```

&nbsp;

# Credits
Originally forked from https://github.com/PappaStalin/Spotify-Lyrics  

I have refactored code to my tastes, including switching to use the simpler oauth mechanism / removing dependency on Spotipy and HTTP servers, which caused a tricky setup process.
