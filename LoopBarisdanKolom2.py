import time

awalbaris=1
akhirbaris=5
stringbintang=""
while(awalbaris<=akhirbaris):
    #loopingkolom
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