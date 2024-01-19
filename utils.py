import pyshorteners


def create_short_url(url: str) -> str:
    short_url = pyshorteners.Shortener()
    return short_url.tinyurl.short(url)