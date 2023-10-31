#import kitap_islemleri
import json
#import os
#import zaman


#uye_id = 1

#uye.json dosyasi yazma olusturma
#def uye_guncelle(uye):


# uye.json dosyasi yazma olusturma
#def uye_kontrol():

# uye ekle
# `uye.json` dosyasından üye bilgilerini yükle

try:
    with open("uye.json", "r", encoding="utf-8") as json_dosyasi:
        # Eğer dosya mevcutsa mevcut üye bilgilerini yükleyin
        Uyeler = json.load(json_dosyasi)
except FileNotFoundError:
    # Eğer dosya bulunmuyorsa veya mevcut değilse, boş bir liste ile başlayın
    Uyeler = []



def uye_ekle():
    Uye_Adi = input("Uye adi giriniz : ")
    Tel = input("Uye telefon giriniz : ")
    Adres = input("Uye adres giriniz : ")
    Uye = {
        "Uye Numarası":  max(uye['Uye Numarası'] for uye in Uyeler) + 1,
        "Uyenin Adı": Uye_Adi,
        "Telefon": Tel,
        "Adres": Adres
    }
    Uyeler.append(Uye)
    print(f"{max(uye['Uye Numarası'] for uye in Uyeler)} id numarali {Uye_Adi} uyesi eklendi.")
    with open("uye.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Uyeler, json_dosyasi, ensure_ascii=False, indent=4)
    

def uye_listeleme():
    for uye in Uyeler:
        print(uye)
    print("Kütüphanedeki aktif üye sayısı= ", len(Uyeler))



# uye arama
def uye_ara():
    ara= input("Uye adı yada id giriniz : ")
    for uye in Uyeler:
        if ara==uye["Uyenin Adı"] or ara==str(uye["Uye Numarası"]):
            print(uye)
            break
    else:
        print("Aradığınız uye bulunamadı.")
    
    

# uye_sil
def uye_sil():
    silinecek_uye = int(input("Silinecek uyenin numarasını girin: "))
    for uye in Uyeler:
        if uye["Uye Numarası"] == silinecek_uye:
            Uyeler.remove(uye)
            print(f"'{uye['Uyenin Adı']}' isimli uye silindi.")
            break
    else:
        print("Belirtilen uye numarasına sahip uye bulunamadı.")
    with open("uye.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Uyeler, json_dosyasi, ensure_ascii=False, indent=4)



# uye okuyucuya kitap verme (tarih islemlerini burada yapacaksin)
def kitap_odunc_verme():
    pass


# Üye bilgilerini JSON dosyasına kaydedin



"""

# takip.json dosyasini burada olusturup yazacaksin
def takip_yaz(veri):


# takip.json dosyasini burada okuyacaksin
def takip_oku():



def kitap_iade():pass




if __name__ "__main__":
    kitap_odunc_verme()
    
"""
