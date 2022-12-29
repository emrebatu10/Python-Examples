print("100 lira ve üzeri alışverişlerde 10 tl , 50 lira ve üzeri alışverişlerde 5 tl indirim.")
urun_fiyat = int(input("ürün fiyatını giriniz : "))

if urun_fiyat >=50 and urun_fiyat < 100:
    print("indirim oranı 5 tl")
    print("Ürünün fiyatı {} liradır".format(urun_fiyat-5))



elif urun_fiyat > 100:
    print("indirim oranı 10 tl")
    print("Ürünün fiyatı {} liradır".format(urun_fiyat-10))



elif  urun_fiyat > 0 and urun_fiyat < 50:
    print("indirim oranı 0 tl")
    print("Ürünün fiyatı {} liradır".format(urun_fiyat))