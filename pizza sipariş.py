print("ANKARA PİZZA HOUSE'A HOŞGELDİNİZ")

boyut=input('Pizzanız hangi boy olsun?:"Küçük boy","Orta boy"veya"Büyük boy"')
ekstra_sos=input('Ekstra sos ister misiniz?:"Evet","Hayır"')
icecek=input('İçecek ister misiniz?:"Evet","Hayır"')

hesap=0
if boyut=="Küçük boy":
    hesap+=35
elif boyut=="Orta boy":
    hesap+=55
else:
    hesap+=75

if ekstra_sos=="Evet":
    if boyut=="Küçük boy":
        hesap+=7
    else:
        hesap+=8
if icecek=="Evet":
    hesap+=4
print(f"Hesabınız toplam tutarı:{hesap} ₺")
