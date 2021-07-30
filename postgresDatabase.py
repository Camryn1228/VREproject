import psycopg2



def insert_table1_list(table1_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO table1(col2) VALUES(%s)"
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="malwaresim", user='postgres', password='peaCeandlove', host='127.0.0.1', port= '5432')
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,table1_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)







def fetch_table_data(table1):
        # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
        cnx = psycopg2.connect(database="malwaresim", user='postgres', password='peaCeandlove', host='127.0.0.1', port= '5432')

        cursor = cnx.cursor()
        cursor.execute('Select * FROM ' + table1)

        header = [row[0] for row in cursor.description]

        rows = cursor.fetchall()

        # Closing connection
        cnx.close()

        return header, rows



insert_table1_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])





