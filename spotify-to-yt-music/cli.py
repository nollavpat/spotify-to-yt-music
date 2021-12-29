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
@click.option("--title", help="Playlist title.")
def create_yt_playlist(playlist_id, title):
    spotify_playlist = spotify_api.get_playlist_songs(playlist_id)
    video_ids = []

    for spotify_song in spotify_playlist:
        yt_song = yt_music_api.get_video_id(spotify_song)
        video_ids.append(yt_song["video_id"])

    yt_music_api.create_playlist(title, video_ids, playlist_id)


cli.add_command(yt_setup, name="yt-setup")
cli.add_command(create_yt_playlist, name="create-yt-playlist")

if __name__ == "__main__":
    cli()
