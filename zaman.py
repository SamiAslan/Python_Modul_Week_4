from datetime import datetime, timedelta
import json

def tarih():
    simdiki_zaman = datetime.now()
    iade_tarihi = simdiki_zaman + timedelta(days=14)


    simdiki_zaman_str = simdiki_zaman.strftime("%d-%m-%Y %H:%M")
    iade_tarihi_str = iade_tarihi.strftime("%d-%m-%Y")


    # JSON verisini oluşturun
    kitap_bilgisi = {
        "odunc_tarihi": simdiki_zaman_str,
        "iade_tarihi": iade_tarihi_str
    }

    # JSON dosyasını açın veya oluşturun
    with open("takip.json", "w") as json_dosyasi:
        # JSON verisini dosyaya yazın
        json.dump(kitap_bilgisi, json_dosyasi)
    return f"alinan tarih : {simdiki_zaman_str}, | iade tarihi: {iade_tarihi_str}"


#print("alinan tarih :", simdiki_zaman_str, " | ", "iade tarihi:", iade_tarihi_str)


if __name__ == "__main__":
    print(tarih())
#
#
#
#
#
#
# Kitap ödünç verme işlemi yapılırken mutlak suretle
# kitabin ödünç verildigi tarih ve saat ve 2 hafta sonra iade edecek şekilde tarih bilgisi eklenmelidir
# ve bu bilgiler takip.json dosyasına kaydedilmelidir
#
#
# bu işlemi kendi oluşturduğumuz zaman py modulunden yapacağız.
# alinan tarih : 20-09-2023 , 10:38 | iade tarihi : 04-10-2023