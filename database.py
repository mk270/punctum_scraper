
# Punctum Scraper, (c) Martin Keegan, Open Book Publishers, 2019.
# To the extent if any to which this code is subject to copyright, it is
# available under the Apache Licence v2.0

import os
from sqlite3 import dbapi2 as sqlite

sqlite_db_path = os.path.join(os.path.dirname(__file__),
                              'punctum_cover_cache.db')

def get_cache_db_handle():
    """Return a database handle to the DB; create the DB and initialise
       it with a schema if the file does not already exist."""
    create = not os.path.exists(sqlite_db_path)
    db = sqlite.connect(sqlite_db_path)
    if create:
        c = db.cursor()
        c.execute('''create table cover (doi text unique not null,
                                         cover_url text not null);''')
        db.commit()
    return db

def cached(db, doi):
    c = db.cursor()
    args = (doi, )
    c.execute('''select cover_url from cover where doi = ?;''', args)
    res = c.fetchone()
    c.close()
    if res is None:
        return None
    return res[0]

def save_to_cache(db, doi, url):
    c = db.cursor()
    args = (doi, url)
    c.execute('''insert into cover (doi, cover_url) values (?, ?);''', args)
    db.commit()
    c.close()
