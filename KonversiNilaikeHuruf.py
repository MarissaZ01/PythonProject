print("Konversi Nilai ke Huruf")
print ("80 - 100 : A ")
print ("70 - 79 : B ")
print ("60 - 69 : C ")
print ("50 - 59 : D ")
print ("0 - 49 : E ")
Input = int(input("Ketik nilaimu range: (0-100):"))
if Input >=0 and Input <=49 : 
    print ("Nilai mu 'E' (Perbaiki lagi ya)")
else :
    if Input >=50 and Input <=59 :
        print ("Nilai mu 'D'(Perbaiki lagi ya)")
    else :
        if Input >=60 and Input <=69 : 
            print ("Nilai mu 'C' (Ayo semangat)")
        else :
            if Input >=70 and Input <=79 :
                print ("Nilai mu 'B'(Ayo Sedikit lagi)")
            else :
                if Input >=80 and Input <=100 : 
                    print ("Nilai mu 'A' (Yeay Kamu Hebat !)")
                