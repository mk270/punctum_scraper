
# Punctum Scraper, (c) Martin Keegan, Open Book Publishers, 2019.
# To the extent if any to which this code is subject to copyright, it is
# available under the Apache Licence v2.0

import oapen
import csv

def get_punctum_books(path):
    """Return a lazy list of tuples of information about Punctum's books,
       given a CSV file of their metadata, in the form:

       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       (DOI, OAPEN ID, { arbitrary stuff from CSV file }),
       ..."""
    puncsv = csv.DictReader(open(path))
    for row in puncsv:
        doi = row['DOI'].strip("\n")
        doc_type = row['Type of Document']
        oapen_url = row['OAPEN URL']
        assert doc_type in ['Book', 'Journal']
        if doc_type != 'Book':
            continue
        if "oapen.org" not in oapen_url:
            continue
        oapen_id = oapen.get_oapen_id(oapen_url)
        yield doi, oapen_id, row
