import urllib.parse as urlparse

def get_oapen_id(url):
    """Given a URL for a book on OAPEN, extract its OAPEN resource id."""
    assert "oapen.org" in url
    assert "http" in url
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)['docid'][0]

