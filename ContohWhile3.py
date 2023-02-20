import time

start=0
finish=10

while(start<finish):
    if start==1:
        print(start)
        nilaike=start
    if start>=2:
        nilaike=(nilaike*2)+1
        print (nilaike)
    time.sleep(1)
    start+=1
    