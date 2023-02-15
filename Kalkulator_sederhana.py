# Start Code Here
import time
print("Kalkulator Sederhana")
print("-----------------------------------------------------------")
time.sleep(1)
print("Pilih Proses")
time.sleep(1)
print("1. Penjumlahan")
time.sleep(0.5)
print("2. Pengurangan")
time.sleep(0.5)
print("3. Perkalian")
time.sleep(0.5)
Pilihan = input("Masukkan pilihan :")
print("=====================================")
if Pilihan == "1":
  bil1 = int(input("Masukan Bilangan 1 :"))
  bil2 = int(input("Masukan Bilangan 2 :"))
  Hasil = bil1 + bil2
  print("Hasil :")
  print(Hasil)
elif Pilihan == "2":
  bil1 = int(input("Masukan Bilangan 1 :"))
  bil2 = int(input("Masukan Bilangan 2 :"))
  Hasil = bil1 - bil2
  print("Hasil :")
  print(Hasil)
elif Pilihan == "3":
  bil1 = int(input("Masukan Bilangan 1 :"))
  bil2 = int(input("Masukan Bilangan 2 :"))
  Hasil = bil1 * bil2
  print("Hasil :")
  print(Hasil)
