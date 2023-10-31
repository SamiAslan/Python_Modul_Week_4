import json
import os


#kitap.json dosyasi okunur
try:
    with open("kitap.json", "r", encoding="utf-8") as json_dosyasi:
        Kitaplar = json.load(json_dosyasi)
            # Eğer dosya mevcutsa mevcut üye bilgilerini yükleyin
except FileNotFoundError: # Eğer dosya bulunmuyorsa veya mevcut değilse, boş bir liste ile başlayın
    Kitaplar = []

# kitap.json dosyasina verileri yazdirir
def kayit(veri):
    with open("kitap.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Kitaplar , json_dosyasi, ensure_ascii=False, indent=4)

def kitaplar():
    
    for kitap in Kitaplar:
        print(kitap)
    print("Kütüphanede bulunan kitap sayısı= ", len(Kitaplar))

# kitap ekleme
def kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod):
    kitap = {
        "Barkod": Barkod,
        "Dil": "Türkçe",
        "Fiyat": 0,
        "Kitap_Adi": Kitap_Adi,
        "Yayinevi": Yayinevi,
        "Yazar": Yazar
    }
    Kitaplar.append(kitap)
    print(f"{kitap['Barkod']} barkodlu {Kitap_Adi} kitabı eklendi.")
    with open("kitap.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Kitaplar, json_dosyasi, ensure_ascii=False, indent=4)

# kitap silme
def kitap_sil(silinecek_veri):
    pass
# kitap arama
def kitap_ara():
    ara= input("Kitap adını giriniz : ")
    bulunan_kitap=[]
    for kitap in Kitaplar:
        if ara in kitap["Kitap_Adi"]:
            bulunan_kitap.append(kitap)
    else:
        print("Aradığınız uye bulunamadı.")
    print(*bulunan_kitap)

"""
if __name__ "__main__":
    print("islem")

"""







