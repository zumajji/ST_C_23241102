print("silahkan masukkan operasi yang diinginkan")
print("1 - operasi penjumlahan")
print("2 - operasi pengurangan")
pilihan = int(input("masukkan pilihan anda :"))

if pilihan == 1:
    print("ini operasi penjumlahan")
    bilangan1 =  int(input("masukkan bilangan pertama :"))
    bilangan2 = int(input("masukkan bilangan kedua :"))
    hasil = bilangan1 + bilangan2
    print("hasil adalah : ",hasil)
elif pilihan == 2:
    print("ini operasi pengurangan")
    bilangan1 =  int(input("masukkan bilangan pertama :"))
    bilangan2 = int(input("masukkan bilangan kedua :"))
    hasil = bilangan1 - bilangan2
    print("hasil adalah : ",hasil)

