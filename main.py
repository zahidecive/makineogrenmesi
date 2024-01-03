import tkinter as tk
from tkinter import ttk, messagebox

film_turleri = {
    "komedi": [("Londra Merkez", 9.8), ("Tosun Paşa", 8.9), ("Kardeş Payı", 8.9)],
    "aksiyon": [("Jack Ryan", 8.0), ("Karayip Korsanları: Ölü Adamın Sandığı", 7.4), ("Diriliş: Ertuğrul", 7.9)],
    "dram": [("İsyan Gezegeni - Birinci Bölüm: Ateşin Çocuğu", 5.7), ("Muhteşem Yüzyıl", 6.9), ("Atatürk 1881 - 1919", 8.9)],
    "romantik": [("Ağır Romantik", 4.1), ("Aykut Enişte 2", 6.5), ("Aşk Taktikleri", 5.3)],
    "suç": [("Lupin", 7.5), ("Sihirbazlar Çetesi", 7.2), ("Sihirbazlar Çetesi 2", 6.4)],
    "korku": [("Çığlık", 7.4), ("Testere X", 6.6), ("Testere 8: Jigsaw Efsanesi", 5.7)],
    "bilim kurgu": [("Yıldızlararası", 8.7), ("Avengers", 8.0), ("Avatar", 7.9)],
}

def film_oner(tur):
    if tur.lower() in film_turleri:
        film_listesi = film_turleri[tur.lower()]
        en_yuksek_puanli_film = max(film_listesi, key=lambda x: x[1])
        return en_yuksek_puanli_film
    else:
        return None

def film_oner_ve_goster():
    secilen_tur = tur_entry.get().strip()
    sonuc = film_oner(secilen_tur)

    if sonuc:
        messagebox.showinfo("Film Önerisi", f"Önerilen film: {sonuc[0]}\nIMDb Puanı: {sonuc[1]}")
    else:
        messagebox.showerror("Hata", "Geçersiz film türü. Lütfen doğru bir tür girin.")

# Ana pencere oluştur
ana_pencere = tk.Tk()
ana_pencere.title("Film Önerici")

# Stil temasını kullan
stil = ttk.Style()
stil.theme_use("clam")

# Tür girişi
tur_label = ttk.Label(ana_pencere, text="Film Türü:")
tur_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

tur_entry = ttk.Entry(ana_pencere, width=20)
tur_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Öneri butonu
oneri_butonu = ttk.Button(ana_pencere, text="Film Öner", command=film_oner_ve_goster, style="TButton")
oneri_butonu.grid(row=1, column=0, columnspan=2, pady=10)

# Stil ayarları
stil.configure("TButton", padding=5, font=('Helvetica', 10, 'bold'), foreground='white', background='#4CAF50')

# Pencereyi açık tut
ana_pencere.mainloop()
