#program login
str1=input("Input your Username: ")
str2=input("Input your Password: ")
count=0
with open('Username.txt','r') as fileuser :
    for cek in fileuser :
        if str1 in cek :
            count+=1
            str3=cek.rstrip('\n')
            passwd=str3.split(',')
            if str2==passwd[1]:
                count+=1

if count==2:
    print("Welcome", str1)
else :
    print("Sorry, the Id Doesn't exsit...")
    
    