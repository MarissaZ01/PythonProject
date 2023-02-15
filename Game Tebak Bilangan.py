print("Tebak Bilangan")
print('================')
print('\n')
import time
import random

kecil=9
besar=11
while True :
    com=random.randint(1,11)
    print(com)
    
    y=input("Ketik Nilai Kecil/Besar :")
    if com <=9:
        hasil='kecil'
    if com >9 :
        hasil='besar'
    time.sleep(1)
    if y == hasil :
        print('kamu menang')
    if y!=hasil : 
        print('kamu kalah')
    time.sleep(2)

