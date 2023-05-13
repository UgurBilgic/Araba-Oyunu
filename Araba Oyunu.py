başladı = False        

print("Oyunu öğrenmek için 'yardım' komutunu kullanabilirsiniz.")

while True:     
    komut = input(">>> ").lower()
    if komut == "başla":
        if başladı:
            print("Araba zaten ilerliyor!!!")
        else:
            print("Araba ilerlemeye başladı")
            başladı = True  
    elif komut == "dur":
        if not başladı:
            print("Araba zaten durgun halde!!!")
        else:
            print("Araba durdu")
            başladı = False
    elif komut == "yardım":
        print("""
başla  - Başlamak için
dur    - Durmak için
yardım - Yardım için
çıkış  - Çıkış yapmak için
              """)
    elif komut == "çıkış":
        print("Çıkış yapıldı, görüşmek üzere")
        break
    else:
        print("Üzgünüm bu kodu anlamadım, yardım için 'yardım' komutunu kullanabilirsiniz")

input("Çıkmak için ENTER'a basınız")
        