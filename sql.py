import sqlite3

with sqlite3.connect("sample.db") as connection:
    c=connection.cursor()
    # c.execute("""DROP TABLE POSTS""")
    c.execute("""CREATE TABLE POSTS(TITLE TEXT, DESC TEXT)""")
    c.execute('INSERT INTO POSTS VALUES("GOOD","1")')
    c.execute('INSERT INTO POSTS VALUES("GOOD2","2")')