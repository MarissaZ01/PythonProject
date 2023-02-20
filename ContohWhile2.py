import time

start=0
finish=10

while(start<=finish):
    if start%2==0:
        print(start, ": adalah bilangan Genap")
    time.sleep(1)
    start+=1
print("\n")
start=0
finish=10

while(start<=finish):
    if start%2==1:
        print(start, ": adalah bilangan Ganjil")
    time.sleep(1)
    start+=1