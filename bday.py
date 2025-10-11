import datetime
import random
ay_gunleri = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#rastegele tarih 
r_ay = random.randint(1,12)
r_gun =random.randint(1,28)
d_gunu = datetime.datetime(2025,r_ay,r_gun)
print("doğum günün",d_gunu)

for i in range(3):
    print(f"Tahmin hakkın: {3-i}")
#kullanıcı tahmini al 
    
    t_ay = int(input("bir ay tahmin et:"))
    while t_ay <1 or t_ay > 12:
        print("Hatalı ay girdiniz! 1-12 arasında bir sayı girmelisiniz.")
        t_ay = int(input("Bir ay tahmin ediniz:"))
    
    
    t_gun = int(input(f"bir gün tahmin et (1-{ay_gunleri[t_ay]}):"))
    while t_gun<1 or t_gun > ay_gunleri[t_ay]:
        print(f"Hatalı gün girdin!")
        t_gun = int(input("Bir daha gün giriniz "))

    t = datetime.datetime(2025,t_ay,t_gun)

#tahmin ile bilgisayar tahminini karşılama 
#doğruysa kazanırsın,yanlışsa kaç gün fark olduğunu gösterip ipucu 

    if d_gunu == t :
        print("Tebrikler doğru tahmin ettiniz")
        break
    elif t < d_gunu :
        print("Daha ileri bir tarih seçmelisin")
    else:
        print("Daha önce bir tarih seçmelisin ")
else :
        print("Tahmin hakkınız bitti!!!!!!!")
        print("Doğru tahmin uydu :",d_gunu)