
# Punctum Scraper, (c) Martin Keegan, Open Book Publishers, 2019.
# To the extent if any to which this code is subject to copyright, it is
# available under the Apache Licence v2.0

import urllib.parse as urlparse

def get_id(url):
    """Given a URL for a book on OAPEN, extract its OAPEN resource id."""
    assert "oapen.org" in url
    assert "http" in url
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)['docid'][0]

