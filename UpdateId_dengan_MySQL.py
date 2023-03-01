#koneksi
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='latihan'
    )

kunci=int(input("Pilih ID yang akan di ubah: "))
userbaru=input("Nama Usernya: ")
passbaru=input("Passwordnya: ")
#teknik 1
#sql_query="Update user set username='"+userbaru+"',password='"+passbaru+"'where iduser='"+str(kunci)+"'"

#teknik 2
cursor=mydb.cursor()
cursor.execute("""
       UPDATE user
       SET username=%s, password=%s
       WHERE iduser=%s
    """, (userbaru,passbaru,kunci))
#print=sql_query
#cursor.executed(sql_query)
print("Data berhasil di perbarui!")
mydb.commit()
mydb.close()
#else:
    #print("Sorry, the Id Doesn't exsit...")
    
    