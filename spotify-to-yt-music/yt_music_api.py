from ytmusicapi import YTMusic


def setup(headers_raw):
    YTMusic.setup(filepath="headers_auth.json", headers_raw=headers_raw)


def get_video_id(song_query):
    ytmusic = YTMusic("headers_auth.json")
    result = ytmusic.search(
        query=song_query,
        filter="songs",
    )

    # trust that first result is the closest xaxaxaxa
    return {
        "video_id": result[0]["videoId"],
        "title": result[0]["title"],
        "artists": result[0]["artists"],
    }
