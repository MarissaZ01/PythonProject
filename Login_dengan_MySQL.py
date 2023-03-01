#koneksi
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='latihan'
    )
str1=input("Input your Username: ")
str1=str1.lower()
str2=input("Input your Password: ")
str2=str2.lower()
sql_query='SELECT * FROM user'
cursor=mydb.cursor()
cursor.execute(sql_query)
records=cursor.fetchall()
count=0
for row in records:
        #print('Baris 1: ','username: ',row[1],'password: ',row[2])
        if (row[1]==str1 and row[2]==str2):
            count+=1
            break
        else:
            count=0
            continue
        print(str(count))
if count==1:
    print("Welcome", str1)
else:
    print("Sorry, the Id Doesn't exsit...")
    
    