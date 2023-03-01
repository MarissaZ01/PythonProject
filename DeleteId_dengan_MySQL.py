#koneksi
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='latihan'
    )

kunci=int(input("Pilih ID yang akan di hapus: "))
sql_query="DELETE FROM user WHERE iduser='"+str(kunci)+"'"
cursor=mydb.cursor()
cursor.execute(sql_query)
#print=sql_query
#cursor.executed(sql_query)
print("Data berhasil di perbarui!")
mydb.commit()
mydb.close()
#else:
    #print("Sorry, the Id Doesn't exsit...")
    
    