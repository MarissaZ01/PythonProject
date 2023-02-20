import time

print("Menu")
print("Daftar Menu dan Harga")
print("-----------------------------------------------------------")
time.sleep(1)
#price=[5000,10000,25000]
nasi=5000
sayur=10000
ayam=25000
print("1. Nasi :",nasi)
time.sleep(0.5)
print("2. Sayur Sop :",sayur)
time.sleep(0.5)
print("3. Daging Ayam :",ayam)
time.sleep(0.5)
userchoose1 = int(input("Ketik nomor pesanan anda :"))
if userchoose1 == 1:
  acc = userchoose1 - 1
  acc2 = int(input("Ketik jumlah pesanan anda :"))
  caculate = nasi * acc2
  print('Total Harga:' + str(caculate))
if userchoose1 == 2:
  acc = userchoose1 - 1
  acc2 = int(input("Ketik jumlah pesanan anda :"))
  caculate = sayur * acc2
  print('Total Harga:' + str(caculate))
if userchoose1 == 3:
  acc = userchoose1 - 1
  acc2 = int(input("Ketik jumlah pesanan anda :"))
  caculate = ayam * acc2
  print('Total Harga:' + str(caculate))
bayar=int(input("Berapa uang anda :"))
kembalian=bayar-caculate
if kembalian>0:
    print("Kembalian anda: ", kembalian)
else:
    print("Maaf uang anda belum cukup")
