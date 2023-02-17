print("Game Suit")
print('================')
print('\n')
import time
import random

batu=1
gunting=2
kertas=3
while True :
    com=random.randint(1,3)
    tebakan=int(input("Tekan 1 untuk batu, 2 untuk gunting, 3 untuk kertas :"))
    #utk Batu
    if com == 1 and tebakan == 1:
        print("seri")
    else :
        if com == 1 and tebakan == 2:
            print("Komputer Batu(Kalah)")
        else :
            if com == 1 and tebakan == 3:
                print("Komputer Batu, Kamu Kertas (Menang)")
                #utk gunting
                if com == 2 and tebakan == 2:
                      print("seri")
                else :
                    if com == 2 and tebakan == 3:
                        print("Komputer Gunting(Kalah)")
                    else :
                         if com == 1 and tebakan == 2:
                             print("Komputer Batu, Kamu Gunting (Kalah)")
                         else:
                             if com == 3 and tebakan == 2:
                                 print("Komputer Kertas, Kamu Gunting (Menang)")
                                 #utk kertas
                                 if com == 3 and tebakan == 3:
                                       print("seri")
                                 else :
                                     if com == 3 and tebakan == 1:
                                         print("Komputer Kertas (Kalah)")
                                     else :
                                          if com == 3 and tebakan == 2:
                                              print("Komputer Kertas, Kamu Gunting (Menang)")
                                          else:
                                              if com == 1 and tebakan == 3:
                                                  print("Komputer Batu,Kamu Kertas(Menang)")
    time.sleep(2)