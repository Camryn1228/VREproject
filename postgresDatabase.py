import psycopg2


def postgres_database():
   #establishing the connection
   conn = psycopg2.connect(
      database="malwaresim", user='postgres', password='peaCeandlove', host='127.0.0.1', port= '5432'
   )
   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()

   #Executing an MYSQL function using the execute() method
   cursor.execute("select version()")

   # Fetch a single row using fetchone() method.
   data = cursor.fetchone()
   print("Connection established to: ",data)

   #Closing the connection
   return conn.cursor()



postgres_database()




