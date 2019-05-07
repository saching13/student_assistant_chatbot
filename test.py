import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='chatbot'
)

print(mydb)

mycursor = mydb.cursor()
date = '2019-04-17 00:00:00'

mycursor.execute("select event_name,start_time,end_time,venue from events where event_date = %s ",(date,))


myresult = mycursor.fetchall()

print(myresult)
for d in myresult:
    [name,start_time,end_time,location] =d

    start_time = (datetime.datetime.min + start_time).time()
    end_time = (datetime.datetime.min + end_time).time()
    print(type(start_time),end_time,name)




mycursor.close()
mydb.close