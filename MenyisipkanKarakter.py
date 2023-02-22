string1="Marissa"
string2=""

panjang=len(string1)
for i in range(0,panjang):
    if i==4:
        string2=string2+'1234'+string1[i]
    else:
     string2=string2+string1[i]
print(string2)
string2=string2.replace("1234",'')
striing2=string2.removeprefix('a')
print(string2)

