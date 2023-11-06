import sys
import random

def oyun():
    oyun_sayisi = 0
    win_count = 0
    lose_count = 0

    def tahmin():
        nonlocal oyun_sayisi, win_count, lose_count
        isim = input("Lütfen isminizi giriniz: ")
        player = int(input(f"Merhaba, {isim} lütfen 1-3 arasında bir sayı tahmin ediniz: "))
        print(f"Seçtiğiniz sayı; {player}")
        computer = random.choice(range(1, 4))
        print(f"Bilgisayarın tuttuğu sayı; {computer}")
        if player == computer:
            print("Tebrikler Bildiniz!")
            win_count += 1
            print(f"Galibiyet Sayısı: {win_count}")
        else:
            print("Maalesef bilemediniz")
            lose_count += 1
            print(f"Yenilgi Sayısı: {lose_count}")

        oyun_sayisi += 1
        print(f"Oyun Sayısı: {oyun_sayisi}")
        def devam1():
            devam = input("Oyuna devam etmek ister misiniz? Evet için 'E', Hayır için 'H' yazınız: ").lower()

            if devam == "e":
                tahmin()
            elif devam == "h":
                sys.exit(f"Oynadığınız için teşekkürler. Skorunuz: {win_count}")
            else:
                print("Geçerli bir komut giriniz")
                devam1()
        devam1()
    tahmin()
if __name__ == "__main__":
    oyun()


