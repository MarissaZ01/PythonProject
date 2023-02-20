import time

start=5
finish=1
hasil=0
strfaktorial=""
print("Nilai Faktorial dari 5 adalah:")
while(start>=finish):
    if start==5:
        hasil=start
        print(hasil)
        strfaktorial=strfaktorial+str(hasil)
    else:
        strfaktorial=strfaktorial+" x "+str(start)
        hasil=hasil*start
        print(strfaktorial,"=",hasil)
    time.sleep(1)
    start-=1
    