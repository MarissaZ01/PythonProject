#Cara 1
string1='malayalam'
temp=''
string2=''
panjangstring=len(string1)
jumlahcocok=0
print(string1==string1[::-1])

#Cara 2
string1=input("Tulis kata polindrome: ")
print(string1==string1[::-1])