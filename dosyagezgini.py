#listeleme,dosya sil,dosya yeniden adlandır,klasöre gir,çık 
import os
def listele():
    print("\nKlasör içeriği:")
    for i in os.listdir(): #listenin içindekileri tektek dolaş 
        print("_",i) #her öğeyi ekrana yazdır
#Kullanıcı listele dediğinde klasörde ne var görmek istiyor.Bu fonksiyon onu yapıyor.


def dosya_sil():
    dosya  = input("Silinecek dosyanın ismi:")
    if os.path.isfile(dosya): #gerçekten bu bir dosya mı?
        os.remove(dosya) #dosyayı sil
        print(f"{dosya} silindi.")
    else:
        print("Böyle bir dosya yok!") 
 #Yanlışlıkla klasör silmemek için kontrol yapıyoruz.Kullanıcı sadece gerçek dosyaları silebiliyor.       


def dosya_yeniden_adlandir():
    eski = input("Eski dosya adı:")
    if os.path.isfile(eski): #dosya var mı?
        yeni = input("Yeni dosya adı:")
        os.rename(eski,yeni) #dosyayı yeniden adlandır
        print(f"{eski} dosyasının adı {yeni} olarak değiştirildi.")
#Kullanıcı dosyanın adını değiştirmek isterse bunu güvenli bir şekilde yapıyoruz.



def klasore_gir():
    secim = input("Girmek istediğiniz klasör adı:")
    if os.path.isdir(secim):
        os.chdir(secim) #klasöre gir
        print("Yeni konum:",os.getcwd())
    else:
        cevap = input("Klasör yok. Oluşturmak ister misin? (E/H): ").lower()
        if cevap == "e":
            os.mkdir(secim)
            print(f"{secim} klasörü oluşturuldu.")
#kullanıcı istediği klasöre güvenli bir şekilde geçebiliyor veya yeni klasör oluşturabiliyor.
