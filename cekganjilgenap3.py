import random
import time

while True : 
    Input = random.randint(1,100)
    print ('menentukan bilangan ganjil dan genap')
    if Input <1 or Input >100 : 
        print ("Exit from the Program")
    else :
        hasilbilangan=Input%2 #modulus adalah untuk menghitung sisa hasil bagi
        if hasilbilangan==0:
            print (Input,"adalah Bilangan Genap")
        else :
            print (Input,"adalah Bilangan Ganjil")
        time.sleep(2)