# Sadece Fonksiyon kullanılarak yazılmıştır.

def paracek(para):
    deger=0
    deger = para // 200
    print (f"200lük sayisi : {deger}")
    para = para % 200
    deger = para // 100
    print (f"100lük sayisi : {deger}")
    para = para % 100
    deger = para // 50
    print (f"50lik sayisi : {deger}")
    para = para % 50
    deger = para // 20
    print (f"20lik sayisi : {deger}")
    para = para % 20
    deger = para // 1
    print (f"1lik sayisi : {deger}")
    para = para % 1



miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))

paracek(miktar)
    
    