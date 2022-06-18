#!/usr/bin/env python3
import os #os kütüphanesini import ediyoruz
def şifrele(): #şifreleme fonksiyonunu oluşturuyoruz.
    def cls():
        if os.name =='nt': #os ile dosya ve dizinlerde arama işlemini yapıyoruz.
            os.system("cls")
        else:
            os.system("clear")
    şifrelim="" #bu değer input değerinden gelecek
    cls()
    metin = input("Şifrelemek istediğiniz metni giriniz ")
    cls()
    while True:
        anahtar=int(input("Anahtar belirtiniz anahtar doğal sayı olmalı: "))
        if int(anahtar) < 0:
            print("Tekrar deneyin..\n Nütfen pozitif sayı giriniz ")
            input()
            cls()
        else:
            cls()
            break
    for harf in metin:
        if ord(harf) == 32: #ord fonksiyonu ile gönderilen temsili değeri 32 ye eşit mi değil mi
            şifrelim += " " #eşit ise şifrelimin üzerin ekliyor.
        şifrelim = şifrelim+chr(ord(harf)+anahtar)#şifrelim fonksiyonu karakter ve anahtar ile toplanıyor.
    print("İşlem başarılı, şifrelenen metin"," ' ",şifrelim," ' ")
    input()
def şifreçöz():
    def cls():
        if os.name =='nt':
            os.system("cls")
        else:
            os.system("clear")
    şifrelim=""
    cls()
    metin=input("Çözmek istediğiniz metni giriniz ")
    cls()
    while True:
        anahtar=int(input("Anahtar belirtiniz (pozitif sayi olucak anahtar) ")) #offset değeri giriliyor.
        if int(anahtar) < 0: #anahtarın 0 dan küçük olamayacağı belirtiliyor.
            cls()
            print("Tekrar deneyin..\n Nütfen pozitif bir anahtar belirtiniz")
            input()
            cls()
        else:
            cls()
            break
    for harf in metin:
        if ord(harf) == 32:
            şifrelim += " "
        else:
            şifrelim += chr(int(ord(harf)-anahtar)) #burada girilen ofset değerindenden metin çıkarılıyor.
    print("İşlem başarılı, çözülen metin"," ' ",şifrelim," ' ")
    input()

def main():
    def cls():
        if os.name =='nt':
            os.system("cls")
        else:
            os.system("clear")
    tercih_1=input(" Metin çözmek için 1'e...\n Yeni metin şifrelemek için ise 2'ye basınız...")
    if tercih_1=="1":
        cls()
        şifreçöz()
        cls()
        cya=input("Programı yeniden başlatmak için y,\n kapatmak içinse herhangi bir tuşa basınız ")
        if cya=="y":
            cls()
            main()
        else:
            cls()
            exit()
    if tercih_1=="2":
        cls()
        şifrele()
        cls()
        cya=input("Programı yeniden başlatmak için y,\n kapatmak içinse herhangi bir tuşa basınız ")
        if cya=="y":
            cls()
            main()
        else:
            cls()
            exit()
if __name__=='__main__':
    main()