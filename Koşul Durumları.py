
print("1-TOPLAMA , 2-ÇIKARMA , 3-ÇARPMA , 4-BÖLME")
sayı_1 = int(input("Sayı 1:"))
sayı_2 = int(input("Sayı 2:"))
islem = int(input("Yapmak istenilen işlemi seçiniz:"))

if islem == 1:
    print(sayı_1 + sayı_2)

elif islem == 2:
    print(sayı_1 - sayı_2)

elif islem == 3:
    print(sayı_1 * sayı_2)

elif islem == 4:
    print(sayı_1 / sayı_2)

else:
    print("Geçersiz işlem")


