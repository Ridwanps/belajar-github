print('halo nama kamu siapa?')
# oke itu kita cuma minta inputan tapi kenapa, tidak langsung disapa dengan menggunakan format
nama = input(nama)
lokasi = input(lokasi)
print(f'halo nama kamu siapa?, oiya kenalin namaku {nama} dari {lokasi}. Salken ya')

# nah misal baru lagi kita akan buat statment itu kedalam sbuah function
def sapa(nama, lokasi):
  print(f'hai namamu {nama} ya? oiya kamu yang asli dari {lokasi} itu bukan?')
  
# deklarasikan dan panggil
sapa(Bambang,Klaten)
sapa(Ridwan,Luzern)
