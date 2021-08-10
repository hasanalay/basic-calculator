print("işlem_1: Toplama")
print("işlem_2: Çıkarma")
print("işlem_3: Çarpma")
print("işlem_4: Bölme")
islem = input("işlemi seçiniz:")
sayi1 = int(input("sayi1:"))
sayi2 = int(input("sayi2:"))
if islem == "1":
    sonuc = int(sayi1) + int(sayi2)
    print("Sonuç:", str(sonuc))
elif islem == "2":
    sonuc = int(sayi1) - int(sayi2)
    print("Sonuç:", str(sonuc))
elif islem == "3":
    sonuc = int(sayi1) * int(sayi2)
    print("Sonuç:", str(sonuc))
elif islem == "4":
    sonuc = int(sayi1) / int(sayi2)
    print("Sonuç:", str(sonuc))
