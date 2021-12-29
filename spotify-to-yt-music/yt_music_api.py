from ytmusicapi import YTMusic


def setup(headers_raw):
    YTMusic.setup(filepath="headers_auth.json", headers_raw=headers_raw)


def testsearch():
    ytmusic = YTMusic("headers_auth.json")
    res = ytmusic.search("twice")

    print(res)
