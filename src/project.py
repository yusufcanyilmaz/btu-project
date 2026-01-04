def pozitif_onluktan_ikilige(n):
    """Pozitif onluk sayıyı matematiksel döngüyle saf binary'ye çevirir."""
    if n == 0:
        return "0"
    res = ""
    gecici = n
    while gecici > 0:
        res = str(gecici % 2) + res
        gecici //= 2
    return res


def bit_tersle(bit_str):
    """Bitleri ters çevirir (1->0, 0->1). İkiye tümleyen için ilk adımdır."""
    ters_str = ""
    for bit in bit_str:
        ters_str += "1" if bit == "0" else "0"
    return ters_str


def bir_ekle(bit_str):
    """Binary katarına matematiksel olarak 1 ekler. İkiye tümleyen için son adımdır."""
    liste = list(bit_str)
    elde = 1
    for i in range(len(liste) - 1, -1, -1):
        if liste[i] == "1" and elde == 1:
            liste[i] = "0"
            elde = 1
        elif liste[i] == "0" and elde == 1:
            liste[i] = "1"
            elde = 0
            break
    return "".join(liste)


def onluktan_ikilige_signed(sayi, bit_sayisi=16):
    """Negatif sayı desteği için Two's Complement (İkiye Tümleyen) hesaplanır."""
    if sayi >= 0:
        return pozitif_onluktan_ikilige(sayi).zfill(bit_sayisi)
    else:
        # Negatif sayı mantığı: Pozitifi bul -> Tersle -> 1 Ekle
        pozitif_ikilik = pozitif_onluktan_ikilige(abs(sayi)).zfill(bit_sayisi)
        terslenmis = bit_tersle(pozitif_ikilik)
        return bir_ekle(terslenmis)


def ikilikten_onaltiliga(ikilik_str):
    """16 bitlik veriyi 4'erli gruplayarak Hexadecimal'e çevirir."""
    hex_sozluk = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5",
        "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    hex_sonuc = ""
    for i in range(0, len(ikilik_str), 4):
        parca = ikilik_str[i:i + 4]
        hex_sonuc += hex_sozluk[parca]
    return hex_sonuc


def bellek_gorseli_ciz(ikilik_str):
    """Belleği 8-bitlik kutucuklar halinde görselleştirir."""
    print("\n[ BELLEK (RAM) GÖRÜNÜMÜ - 16 BIT ]")
    for i in range(0, len(ikilik_str), 8):
        byte_verisi = ikilik_str[i:i + 8]
        print(f"Byte {i // 8}: " + "+---" * 8 + "+")
        bit_satiri = "        "
        for bit in byte_verisi:
            bit_satiri += f"| {bit} "
        print(bit_satiri + "|")
        print("        " + "+---" * 8 + "+")


# --- ANA DÖNGÜ VE PROGRAM KONTROLÜ ---
def program_baslat():
    # Programın sürekli çalışması için sonsuz döngü başlatıyoruz
    while True:
        print("\n" + "=" * 50)
        print("   ÇOK FONKSİYONLU TABAN DÖNÜŞTÜRÜCÜ   ")
        print("=" * 50)
        print("Çıkış yapmak için 'q' tuşuna basabilirsiniz.")

        user_input = input("\nOnluk tabanda bir sayı girin: ")

        # programın bitiş tuşu
        if user_input.lower() == 'q':
            print("Programdan çıkılıyor... İyi günler!")
            break  # Bitiş tuşuna basılınca programı bitirir.

        try:
            # Girdiyi tam sayıya çevirmeyi deniyoruz
            onluk_sayi = int(user_input)

            # 16-bitlik sistem üzerinden bit dizisini hesaplıyoruz
            bit_dizisi = onluktan_ikilige_signed(onluk_sayi, 16)

            print("\nİşlem Seçin:")
            print("1) İkilik (Binary)")
            print("2) Onaltılık (Hexadecimal)")
            print("3) Tüm Dönüşümleri Göster")

            secim = input("Seçiminiz: ")
            print("-" * 30)

            # Seçime göre sonuçları yazdır
            if secim == "1":
                print(f"Sayı: {onluk_sayi} -> Binary: {bit_dizisi}")
            elif secim == "2":
                print(f"Sayı: {onluk_sayi} -> Hex: 0x{ikilikten_onaltiliga(bit_dizisi)}")
            else:
                print(f"Sayı: {onluk_sayi}")
                print(f"Binary: {bit_dizisi}")
                print(f"Hex   : 0x{ikilikten_onaltiliga(bit_dizisi)}")

            # Her durumda bellekte nasıl tutulduğunu gösterir.
            bellek_gorseli_ciz(bit_dizisi)

            # Bir işlem bittikten sonra bir dahaki işleme başlamak için
            input("\nDevam etmek için ENTER'a basın...")

        except ValueError:
            # Eğer int(user_input) hata verirse (harf girilirse vs.) burası çalışır
            print("\n!!! HATA: Lütfen geçerli bir sayı girin veya çıkış için 'q' yazın.")
            # Döngü başına döner, program kapanmaz.


if __name__ == "__main__":
    program_baslat()
