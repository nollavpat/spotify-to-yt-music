import click
import yt_music_api


@click.group()
def cli():
    pass


@click.command()
@click.argument("raw_header")
def ytsetup(raw_header):
    click.echo("Creating headers_auth.json ...")
    yt_music_api.setup(raw_header)


@click.command()
def testsearch():
    click.echo("searching ...")
    yt_music_api.testsearch()


cli.add_command(ytsetup)
cli.add_command(testsearch)

if __name__ == "__main__":
    cli()
