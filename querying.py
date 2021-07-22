# connect to the data base
import psycopg2

conn = psycopg2.connect("your dsn")

# create cursor object
cur = conn.cursor()
cur.execute(SELECT, (vaule1,vaule2))

# use fetch many method to get all data from data base

def getdata (cursor, size=10): #extracts data from multible tables
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def getrows():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute()

        for row in getdata(cur, 10):
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__querying__':
    getrows()

