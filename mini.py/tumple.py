#demet = (10,20,30,40) #eğer veri değişmeyecek ise tumple daha güvenlidir.
#print(demet[0])

#veri = (1,(2,3),[4,5,])
#dışı tumple değişmez ama içi değişebilir.

#demet = (1, 2, 3)
#liste = [1, 2, 3]

#print(len(demet))
#print(len(liste))

#veri = ("Nurseda",19,"Erciyes","Mühendislik")
#veri += veri + ("Tekirdag",) 
#print(veri)
#tuple can be merged but not added 

#kümeler sırasız ve her eleman eşsiz(tekil) olmasıdır.Bu,bir küme içinde aynı elemandan birden fazla bulunamayacağı anlamına gelir.Bir veri setindeki tekrarları temizlemek için kullanılır.Hızlı aramada yapmak için kullanılır.
#ayse_dersleri = ["matematik","fizik","kimya","biyoloji","fizik"]
#ahmet_dersleri = ["matematik","fizik","resim","spor","resim"]

#ayse_kumesi = set(ayse_dersleri)
#ahmet_kumesi = set(ahmet_dersleri)
#print(ayse_kumesi)
#print(ahmet_kumesi)

#bos_kume = set() #boş küme oluşturma
#sayi_kumesi = {1,2,3,4,5} #Eleman içeren bir küme oluşturma 
#Sadece {} yazarsak bu bir sözlük olur.

#sayi_kumesi = {1,2,3,4,5}
#sayi_kumesi.add(6) #küme içine eleman ekleme
#sayi_kumesi.remove(3) #küme içinden eleman silme,belirtilen sayı kümede yoksa hata verir.
#sayi_kumesi.discard(10) #Belirtilen eleman kümede yoksa hata vermez.
#print(sayi_kumesi)

sehirler = {"Ankara","İstanbul","İzmir"}
#kümeye Bursa şehrini ekleme 
#sehirler.add("Bursa")
#İzmir şehrini sil 
#sehirler.remove("İzmir")
#Adana şehrini hata vermeden silmeye çalış 
#sehirler.discard("Adana")
#print(sehirler)

#kume1= {1,2,3}
#kume2 = {3,4,5}
#birlesim = kume1 | kume2 #küme birleşimi
#kume1.union(kume2) #küme birleşimi
#print("Birlesim",birlesim)
#kesisim = kume1 & kume2 #küme kesişimi
#print("Kesisim",kesisim)
#fark = kume1 - kume2 
#print("Fark",fark)

#ayse_dersleri = {"matematik","fizik","kimya","biyoloji","fizik"}
#ahmet_dersleri = {"matematik","fizik","resim","spor","resim"}
#her iksininde altığı tüm dersleri bul.
#tum_dersler = ayse_dersleri | ahmet_dersleri
#print("Tüm dersler:",tum_dersler)
#her iksinin de aldığı ortak dersler
#ortak_dersler = ayse_dersleri & ahmet_dersleri
#print("Ortak dersler:",ortak_dersler)
#ayse'nin aldığı ama ahmet'in almadığı dersler
#farkli_dersler = ayse_dersleri - ahmet_dersleri
#print("Ayşe'nin farklı dersleri:",farkli_dersler)

#dictionary 
#anahtar :değer şeklinde yazılır.Sıralıdırlar.Değiştirilebilirler.
#Bir öğrncinin bilgilerini tutan bir sözlük oluşturalım.
#ogrenci = {
 # "ad":"Karmen",
  #  "soyad":"Yılmaz",
   # "numara:": 123,
    #"bolum":"Endustri Mühendisliği",
     #  "aktif mi" : True
#}
 #print(ogrenci)
 
#Karmen'in bölümünü ekrana yazdır.
#print(ogrenci["bolum"])
#yas = ogrenci.get("yas") #hata vermek yerine none döndürür
#print(yas)
#yeni bir bilgi ekleyelim.
#ogrenci["yas"] = 20
#print(ogrenci)
#mevcut bilgiyi güncelleyelim.
#ogrenci["numara:"]= 674
#print(ogrenci)
#aktif mi bilgisini silelim.
#del ogrenci["aktif mi"]
#print(ogrenci)
#silinen_bolum = ogrenci.pop("bolum") #silinen değeri döndürür.
#print("Silinen bölüm:",silinen_bolum)
#print("Sözlüğün son hali:",ogrenci)

kullanici = {
    "kullanici_adi":"coder",
    "email": "coder@example.com",
    "kayit_tarihi": "2025-10-26"
}
#sadece anahtarlar üzerinde dolaşmak 
#for anahtar in kullanici:
 #   print(anahtar)
 #anahtarlar ve değerleri birlikte kullanmak 
for anahtar,deger in kullanici.items():
        print(anahtar,"=",deger)