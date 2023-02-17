print ('menentukan bilangan ganjil dan genap')
Input = int(input("Masukan Angka mulai dari 2 hingga 10, selain itu tidak ada jawabannya :"))
if Input <2 or Input >10 : #untuk cek inputan sesuai range yang di inginkan
    print ("Bilangan tidak terdeteksi")
else :
    print ("Ini adalah :")
    hasilbilangan=Input%2 #modulus adalah untuk menghitung sisa hasil bagi
    if hasilbilangan==0:
        print ("Bilangan Genap")
    else :
        print ("Bilangan Ganjil")