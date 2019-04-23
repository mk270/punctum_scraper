
# Punctum Scraper, (c) Martin Keegan, Open Book Publishers, 2019.
# To the extent if any to which this code is subject to copyright, it is
# available under the Apache Licence v2.0

import oapen
import csv

def get_books(path):
    """Return a lazy list of tuples of information about Punctum's books,
       given a CSV file of their metadata, in the form:

       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       None,
       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       ...

       None is generated where the data relates to a non-book or something
       otherwise not on OAPEN. It is the responsibility of the caller to
       filter these out."""
    puncsv = csv.DictReader(open(path))
    for row in puncsv:
        doi = row['DOI'].strip("\n")
        doc_type = row['Type of Document']
        oapen_url = row['OAPEN URL']
        assert doc_type in ['Book', 'Journal']
        if doc_type != 'Book':
            yield None
        elif "oapen.org" not in oapen_url:
            yield None
        else:
            oapen_id = oapen.get_id(oapen_url)
            yield doi, oapen_id, row
