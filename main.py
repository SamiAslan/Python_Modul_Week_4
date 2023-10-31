import kitap_islemleri
import uye_islemleri
import json
import os


while(True):
    try:
        print("HALK KUTUPHANEMIZE HOS GELDINIZ")
        print("1 - UYELIK ISLEMLERI 1")
        print("2 - KITAP ISLEMLERI 2")
        print("3 - CIKIS 0")
        secim=input("Lutfen yapmak istediginiz secimin kodunu girin : ", )
        os.system('cls')
        if secim == '1': #UYELIK ISLEMLERI
            while True:
                print("UYELER = 1              &    KITAP ODUNC VERME = 5")
                print("UYE EKLEME = 2          &    KITAP IADE = 6  ")
                print("UYE ARA = 3             &    KITAP TAKIBI = 7")
                print("UYE SIL = 4             &    CIKIS = 0")
                uye_secim=input("Lutfen işlem seciniz : ", )
                if uye_secim=="1": 
                    uye_islemleri.uye_listeleme()
                elif uye_secim=="2": 
                    uye_islemleri.uye_ekle()
                elif uye_secim=="3": 
                    uye_islemleri.uye_ara()
                elif uye_secim=="4": 
                    uye_islemleri.uye_sil()
                elif uye_secim=="4": 
                    uye_islemleri.kitap_odünc_verme()
                elif uye_secim=="0": 
                    break
                
        elif secim == '2':
            while True:
                print("KITAPLAR = 1")
                print("KITAP EKLEME = 2 ")
                print("KITAP ARA = 3")
                print("KITAP SIL = 4 ")
                print("CIKIS = 0")
                kitap_secim=input("Lutfen işlem seciniz : " )
                if kitap_secim=="1": 
                    kitap_islemleri.kitaplar()
                elif kitap_secim=="2": 
                    Kitap_Adi = input("Kitap adi giriniz : ")
                    Yazar = input("Yazar giriniz : ")
                    Yayinevi = input("Yayınevi giriniz : ")
                    Barkod = input("Barkod giriniz : ")
                    kitap_islemleri.kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod)
                elif kitap_secim=="3": 
                    kitap_islemleri.kitap_ara()
                elif kitap_secim=="4": 
                    silinecek_kitap = input("Silinecek kitabın adını girin: ")
                    kitap_islemleri.kitap_sil(silinecek_kitap.upper())
                elif kitap_secim=="0": 
                    break    
        elif secim == '0':
            print("Kütüphane programından çıkılıyor !...")
            break

    except Exception as hata:
        print("Hata : ", hata, end='\n\n')



