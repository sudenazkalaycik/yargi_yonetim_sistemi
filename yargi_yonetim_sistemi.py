from abc import ABC, abstractmethod

print(
    "\n"
    "Sayın kullanıcı, bir dava açmak için şu adımları sırayla takip edebilirsiniz:\n"
    "1) Kişi İşlemleri menüsüne girip Hakim, Avukat, Taraf ekle.\n"
    "2) Mahkeme İşlemleri menüsüne girip Mahkeme ekle.\n"
    "3) Dava İşlemleri menüsüne girip Yeni Dava Aç.\n"
    "Sonrasında dava başarıyla oluşturulacaktır."
)


# ----- Sınıflar -----
class Kisi(ABC):
    def __init__(self, ad, soyad, kimlik_no):
        self.__ad = ad
        self.__soyad = soyad
        self.__kimlik_no = kimlik_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, yeni_ad):
        self.__ad = yeni_ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, yeni_soyad):
        self.__soyad = yeni_soyad

    def get_kimlik_no(self):
        return self.__kimlik_no

    def set_kimlik_no(self, yeni_kimlik_no):
        self.__kimlik_no = yeni_kimlik_no

    @abstractmethod
    def kisi_bilgisi(self):
        pass

class Taraf(Kisi):
    def __init__(self, ad, soyad, kimlik_no):
        super().__init__(ad, soyad, kimlik_no)
        self.Avukat = None

    def kisi_bilgisi(self):
        return (
            f"İsim      : {self.get_ad()}\n"
            f"Soyisim   : {self.get_soyad()}\n"
            f"Kimlik No : {self.get_kimlik_no()}"
        )

class Avukat(Kisi):
    def __init__(self, ad, soyad, kimlik_no, lisans_no, uzmanlik_alani):
        super().__init__(ad, soyad, kimlik_no)
        self.lisans_no = lisans_no
        self.uzmanlik_alani = uzmanlik_alani
        self.muvekkil_listesi = []

    def kisi_bilgisi(self):
        return (
            f"İsim           : {self.get_ad()}\n"
            f"Soyisim        : {self.get_soyad()}\n"
            f"Kimlik No      : {self.get_kimlik_no()}\n"
            f"Lisans No      : {self.lisans_no}\n"
            f"Uzmanlık Alanı : {self.uzmanlik_alani}"
        )

    def muvekkil_ekle(self, muvekkil):
        self.muvekkil_listesi.append(muvekkil)
        muvekkil.Avukat = self
        return "Müvekkil başarıyla listeye eklendi."

    def muvekkil_listesini_goster(self):
        if not self.muvekkil_listesi:
            print("Müvekkil bulunmuyor.")
            return
        print("=== Müvekkil Listesi ===")
        for i, m in enumerate(self.muvekkil_listesi, 1):
            print(f"{i}. {m.get_ad()} {m.get_soyad()}")

class Hakim(Kisi):
    def __init__(self, ad, soyad, kimlik_no, deneyim, dava_sayisi):
        super().__init__(ad, soyad, kimlik_no)
        self.deneyim = deneyim
        self.dava_sayisi = dava_sayisi

    def kisi_bilgisi(self):
        return (
            f"İsim         : {self.get_ad()}\n"
            f"Soyisim      : {self.get_soyad()}\n"
            f"Kimlik No    : {self.get_kimlik_no()}\n"
            f"Deneyim      : {self.deneyim} yıl\n"
            f"Dava Sayısı  : {self.dava_sayisi}"
        )

    def karar_ver(self, dava, karar):
        dava.durum = karar
        return f"Karar verildi: {karar}"

class Dava:
    def __init__(self, dava_no, davaci, davali, hakim, durum, tarih, goruldugu_mahkeme):
        self.dava_no = dava_no
        self.davaci = davaci
        self.davali = davali
        self.hakim = hakim
        self.durum = durum
        self.tarih = tarih
        self.goruldugu_mahkeme = goruldugu_mahkeme

    def durum_guncelle(self, yeni_durum):
        self.durum = yeni_durum
        return f"Dava durumu güncellendi. Yeni durum: {yeni_durum}"

    def detaylari_goster(self):
        return (
            f"\n=== Dava Detayları ===\n"
            f"Dava No: {self.dava_no}\n"
            f"Durum  : {self.durum}\n"
            f"Tarih  : {self.tarih}\n\n"
            f"Hakim Bilgisi:\n{self.hakim.kisi_bilgisi()}\n\n"
            f"Davacı Bilgisi:\n{self.davaci.kisi_bilgisi()}\n\n"
            f"Davalı Bilgisi:\n{self.davali.kisi_bilgisi()}\n\n"
            f"Görüldüğü Mahkeme: {self.goruldugu_mahkeme.ad}\n"
        )

class Mahkeme:
    def __init__(self, ad, adres):
        self.ad = ad
        self.adres = adres

# ----- Uygulama Menüsü -----
def kisi_menu(hakimler, avukatlar, taraflar):
    while True:
        print("\n=== Kişi İşlemleri ===")
        print("1) Hakim Ekle")
        print("2) Avukat Ekle")
        print("3) Taraf Ekle")
        print("4) Avukatın Müvekkil Listesini Gör")
        print("0) Üst Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Hakim Adı: ")
            soyad = input("Hakim Soyadı: ")
            kimlik_no = input("Kimlik No: ")
            deneyim = int(input("Deneyim (yıl): "))
            dava_sayisi = int(input("Baktığı dava sayısı: "))
            hakim = Hakim(ad, soyad, kimlik_no, deneyim, dava_sayisi)
            hakimler.append(hakim)
            print("Hakim eklendi.")
        elif secim == "2":
            ad = input("Avukat Adı: ")
            soyad = input("Avukat Soyadı: ")
            kimlik_no = input("Kimlik No: ")
            lisans_no = input("Lisans No: ")
            uzmanlik = input("Uzmanlık Alanı: ")
            avukat = Avukat(ad, soyad, kimlik_no, lisans_no, uzmanlik)
            avukatlar.append(avukat)
            print("Avukat eklendi.")
        elif secim == "3":
            ad = input("Taraf Adı: ")
            soyad = input("Taraf Soyadı: ")
            kimlik_no = input("Kimlik No: ")
            taraf = Taraf(ad, soyad, kimlik_no)
            taraflar.append(taraf)
            print("Taraf eklendi.")

            # İsteğe bağlı avukata ekleme
            if avukatlar:
                av_secimi = input("Tarafı bir avukata eklemek ister misiniz? (E/H): ")
                if av_secimi.lower() == "e":
                    for i, avu in enumerate(avukatlar, 1):
                        print(f"{i}) {avu.get_ad()} {avu.get_soyad()}")
                    index = int(input("Avukat numarası: "))
                    print(avukatlar[index - 1].muvekkil_ekle(taraf))
        elif secim == "4":
            if not avukatlar:
                print("Ekli avukat bulunmuyor.")
            else:
                for i, av in enumerate(avukatlar, 1):
                    print(f"{i}) {av.get_ad()} {av.get_soyad()}")
                index = int(input("Listesi gösterilecek avukat: "))
                avukatlar[index - 1].muvekkil_listesini_goster()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")

def dava_menu(davalar, taraflar, hakimler, mahkemeler):
    while True:
        print("\n=== Dava İşlemleri ===")
        print("1) Yeni Dava Aç")
        print("2) Dava Detayları Görüntüle")
        print("3) Dava Durum Güncelle")
        print("0) Üst Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            if not taraflar or not hakimler or not mahkemeler:
                print("Önce taraf, hakim ve mahkeme ekleyiniz.")
                continue

            dava_no = input("Dava No: ")
            
            print("Davacı Seçimi:")
            for i, t in enumerate(taraflar, 1):
                print(f"{i}) {t.get_ad()} {t.get_soyad()}")
            davaci_idx = int(input("Seçim: "))
            davaci = taraflar[davaci_idx - 1]

            print("Davalı Seçimi:")
            for i, t in enumerate(taraflar, 1):
                print(f"{i}) {t.get_ad()} {t.get_soyad()}")
            davali_idx = int(input("Seçim: "))
            davali = taraflar[davali_idx - 1]

            print("Hakim Seçimi:")
            for i, h in enumerate(hakimler, 1):
                print(f"{i}) {h.get_ad()} {h.get_soyad()}")
            hakim_idx = int(input("Seçim: "))
            hakim = hakimler[hakim_idx - 1]

            durum = input("Dava Durumu (ör. Devam Ediyor): ")
            tarih = input("Dava Tarihi (YYYY-AA-GG): ")

            print("Mahkeme Seçimi:")
            for i, m in enumerate(mahkemeler, 1):
                print(f"{i}) {m.ad} - {m.adres}")
            mahkeme_idx = int(input("Seçim: "))
            mahkeme = mahkemeler[mahkeme_idx - 1]

            yeni_dava = Dava(dava_no, davaci, davali, hakim, durum, tarih, mahkeme)
            davalar.append(yeni_dava)
            print("Dava başarıyla açıldı.")

        elif secim == "2":
            if not davalar:
                print("Kayıtlı dava yok.")
                continue
            for i, d in enumerate(davalar, 1):
                print(f"{i}) {d.dava_no}")
            d_idx = int(input("Görüntülenecek davanın numarası: "))
            print(davalar[d_idx - 1].detaylari_goster())

        elif secim == "3":
            if not davalar:
                print("Kayıtlı dava yok.")
                continue
            for i, d in enumerate(davalar, 1):
                print(f"{i}) {d.dava_no} - (Durum: {d.durum})")
            d_idx = int(input("Durumu güncellenecek dava: "))
            yeni_durum = input("Yeni durum: ")
            print(davalar[d_idx - 1].durum_guncelle(yeni_durum))

        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")

def mahkeme_menu(mahkemeler):
    while True:
        print("\n=== Mahkeme İşlemleri ===")
        print("1) Mahkeme Ekle")
        print("2) Kayıtlı Mahkemeleri Listele")
        print("0) Üst Menüye Dön")

        secim = input("Seçiminiz: ")
        if secim == "1":
            ad = input("Mahkeme Adı: ")
            adres = input("Mahkeme Adresi: ")
            mahkeme = Mahkeme(ad, adres)
            mahkemeler.append(mahkeme)
            print("Mahkeme eklendi.")
        elif secim == "2":
            if not mahkemeler:
                print("Kayıtlı mahkeme yok.")
            else:
                print("=== Mahkeme Listesi ===")
                for i, m in enumerate(mahkemeler, 1):
                    print(f"{i}) {m.ad} - {m.adres}")
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")

def main():
    hakimler = []
    avukatlar = []
    taraflar = []
    davalar = []
    mahkemeler = []

    while True:
        print("\n====== ANA MENÜ ======")
        print("1) Kişi İşlemleri")
        print("2) Dava İşlemleri")
        print("3) Mahkeme İşlemleri")
        print("0) Çıkış")

        secim = input("Seçiminiz: ")
        
        if secim == "1":
            kisi_menu(hakimler, avukatlar, taraflar)
        elif secim == "2":
            dava_menu(davalar, taraflar, hakimler, mahkemeler)
        elif secim == "3":
            mahkeme_menu(mahkemeler)
        elif secim == "0":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
