import json

import click
import spotify_api
import yt_music_api


@click.group()
def cli():
    pass


@click.command()
@click.argument("raw_header")
def yt_setup(raw_header):
    click.echo("Creating headers_auth.json ...")
    yt_music_api.setup(raw_header)


@click.command()
@click.argument("playlist_id")
def create_yt_playlist(playlist_id):
    spotify_playlist = spotify_api.get_playlist_songs(playlist_id)
    spotify_yt_mapping = []

    for spotify_song in spotify_playlist:
        yt_song = yt_music_api.get_video_id(spotify_song)
        spotify_yt_mapping.append({**yt_song, **{"spotify": spotify_song}})

    with open("mapping.json", "w") as f:
        f.write(json.dumps(spotify_yt_mapping, indent=2))


cli.add_command(yt_setup, name="yt-setup")
cli.add_command(create_yt_playlist, name="create-yt-playlist")

if __name__ == "__main__":
    cli()
