!pip install psycopg2-binary

import psycopg2

dir(psycopg2)

help(psycopg2.connect)
# Looks similar to sqlite3, but needs auth/host info to connect
dbname 'vwzqyejg'
user 'vwzqyejg'
password 'N-svBof1YMFmDMtXHTLDnvIYGyIoVeNO' # sensitive info dont share
host 'isilo.db.elephantsql.com (isilo-01)'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

 pg_curs.execute('SELECT * FROM test_table;')
 pg_curs.fetchall()

insert_statement = """
... INSERT INTO test_table (name, data) VALUES
... (
...   'Zaphod Beeblebrox',
...   '{"key": "value", "key2": true}'::JSONB
... )
... """

pg_curs.execute(insert_statement)
pg_conn.commit()

pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()
pg_curs.close()

 # ETL!

# Extract - Transform - Load

# Extract: get the data out from a source (often the original "source of truth")
# Transform: tweak/change data as appropriate for use case, and to make it fit in...
# Load: Insert data into desired destination

# We'd like to get the RPG data out (extract) of SQLite and insert it into (load) PostgreSQL.

# We may have to tweak it a little (transform), but probably not too much, since both source and destination are SQL databases.

# We're making our first "cloud" ETL!
