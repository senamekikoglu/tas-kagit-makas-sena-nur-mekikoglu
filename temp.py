import random
def tas_kagit_makas():
   liste=["taş","kağıt","makas"] 

   comp=0
   ply=0
    
   print("Taş-Kağıt-Makas Oyununa Hoşgeldiniz!")
   print("")
   print("Kurallar:\n Taş makası ezer. \n Makas kağıdı keser. \n Kağıt taşı sarar.")
   print("Bilgisayara karşı oynayacaksınız ve 2 kez kazanan oyunun galibi olur. Bol şans!")
   print("")
   while ply!=2 and comp!=2:
    players_choice=input("Seçiminiz:").lower()
  
    if players_choice in liste:
       print("Seçiminiz:",players_choice)
    else:
       print("Geçersiz seçim, lütfen tekrar deneyiniz.")
       continue
    
    computers_choice= random.choice(liste)
    print("Bilgisayarın seçimi:",computers_choice)

    if (players_choice=="makas" and computers_choice=="kağıt") or (players_choice=="taş" and computers_choice=="makas") or (players_choice=="kağıt" and computers_choice=="taş"):
       print("Siz kazandınız.")
       ply+=1
    elif players_choice==computers_choice:
       print("Berabere")
    else:
       print("Bilgisayar kazandı.")
       comp+=1
    print("")
    print("Siz-", ply)
    print("Bilgisayar-",comp)
    print("")
   if ply==2:
     print("Tebrikler, oyunu siz kazandınız.")
   else:
     print("Üzgünüm, bilgisayar kazandı.")
     
   kullanici_devam=input("Oyuna devam etmek istiyor musunuz?(evet/hayir):").lower()
   bilgisayar_devam=random.choice(["evet","hayir"])
   print("Bilgisayarın devam kararı:", bilgisayar_devam)
    
    
   while kullanici_devam=="evet" and bilgisayar_devam=="evet":
        print("Yeni oyun başlıyor.")
        tas_kagit_makas()
        break
   if kullanici_devam!="evet" or bilgisayar_devam!="evet":
        print("Oyun sona erdi.")
    
tas_kagit_makas()
     
  