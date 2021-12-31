# spotify-to-yt-music
Import spotify playlist to yt music

### Setup

1. Install dependencies
```
pip3 install -r requirements.txt
```

2. Copy header from https://music.youtube.com. Follow [this](https://ytmusicapi.readthedocs.io/en/latest/setup.html#copy-authentication-headers)

3. Create an application and get `client_id` and `client_secret` from [spotify dashboard](https://developer.spotify.com/dashboard/applications). Create `.env`.

```
# .env
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

### How to use

```
$ python3 spotify-to-yt-music/cli.py --help

Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create-yt-playlist
  yt-setup

# create auth for yt music
$ python3 spotify-to-yt-music/cli.py yt-setup <INSERT RAW HEADER HERE>

# create playlist by providing spotify playlist id
$ python3 spotify-to-yt-music/cli.py create-yt-playlist <INSERT PLAYLIST ID> --title "Tiltle of playlist"
```
testing something
