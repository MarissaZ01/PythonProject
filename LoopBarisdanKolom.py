import time
import random

akhirbaris=5
stringbintang=""
 #loopingkolom
 
while True :
    inputan=random.randint(1,11)
    print("Masukan Angka : ", inputan)
    awalbaris=1
    while(awalbaris<=akhirbaris):
        awalkolom=1
        akhirkolom=awalbaris
        while(awalkolom<=akhirkolom):
           # print("baris:", awalbaris, "kolom :", awalkolom)
            if awalkolom==1:
                stringbintang=" * "
            else :
                stringbintang=stringbintang+" * "
            awalkolom+=1
        print(stringbintang)
        time.sleep(1)
        awalbaris+=1