import mysql.connector
from mysql.connector import Error
x=input()
y=input()
z=int(input())
try :
    connection = mysql.connector.connect(host="localhost",database="k1",user="root",password="109283")
    score_table="""CREATE TABLE score (first_table varchar(20),last_name varchar(20),score int(100))"""
    insert_table=f"""INSERT INTO SCORE_TABLE(first_table,last_name,score) VALUES({x},{y},{z})"""
    cursor =connection.cursor()
    cursor.execute(insert_table)
    result= cursor.execute(score_table)
    connection.commit()
except Exception:
    connection.rollback()
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
