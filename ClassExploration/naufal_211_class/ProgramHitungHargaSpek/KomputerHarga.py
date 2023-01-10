import os

class Komputer:
# inisiasi
    def __init__(self, memori, ram, procesor_Intel, procesor_AMD, layar, resolusi_layar,berat):
    #, harga, ukuran_layar, port_usb, hdmi, wifi, durasi_baterai, , dimensi, merek, sistem_operasi, kamera, speaker
        self.memori = memori
        self.ram = ram
        self.procesor_Intel = procesor_Intel
        self.procesor_AMD = procesor_AMD
        self.layar = layar
        self.resolusi_layar = resolusi_layar
        self.berat = berat
    # self.port_usb = port_usb
    # self.hdmi = hdmi
    # self.wifi = wifi
    # self.durasi_baterai = durasi_baterai
    # self.berat = berat
    # self.dimensi = dimensi
    # self.merek = merek
    # self.sistem_operasi = sistem_operasi
    # self.kamera = kamera
    # self.speaker = speaker
# Membuat fungsi hitung_harga 
    def hitung_harga(self):
        harga_total = 0

        # Memori
        if self.memori == '512':
            harga_total += 650000
        elif self.memori == '1000':
            harga_total += 1300000
        else:
            harga_total += 0

        # Ram
        if self.ram == '4':
            harga_total += 240000
        elif self.ram == '6':
            harga_total += 295000
        elif self.ram == '8':
            harga_total += 380000
        elif self.ram == '16':
            harga_total += 760000
        else:
            harga_total += 0

        # Procesor Intel
        if self.procesor_Intel == '3':
            harga_total += 1300000
        elif self.procesor_Intel == '5':
            harga_total += 3000000
        elif self.procesor_Intel == '7':
            harga_total += 6000000
        elif self.procesor_Intel == '9':
            harga_total += 10000000
        else:
            harga_total += 0

        # procesor AMD
        if self.procesor_AMD == '3':
            harga_total += 1500000
        elif self.procesor_AMD == '5':
            harga_total += 2200000
        elif self.procesor_AMD == '7':
            harga_total += 3300000
        else:
            harga_total += 0

        # jenis Layar
        if self.layar == 'TN':
            harga_total += 1000000
        elif self.layar == 'VA':
            harga_total += 2000000
        elif self.layar == 'IPS':
            harga_total += 3000000
        elif self.layar == 'OLED':
            harga_total += 4000000
        else:
            harga_total += 0
            
        # Resolusi Layar
        if self.resolusi_layar == '1024 x 768':
            harga_total += 1000000
        elif self.resolusi_layar == '1366 x 768':
            harga_total += 2000000
        elif self.resolusi_layar == '1920 x 1080':
            harga_total += 3000000
        else:
            harga_total += 0
        
        # berat
        if self.berat == '1':
            harga_total += 2000000
        elif self.berat == '2':
            harga_total += 3000000
            
        # mengembalikan nilai harga_total
        return harga_total

# meminta input spesifikasi laptop dari user
memori = input('Masukkan jenis memori (512/1000)GB: ')
ram = input('Masukkan jumlah RAM (4/6/8/16)GB: ')
procesor_Intel = input('Masukkan jenis procesor_Intel i(3/5/7/9): ')
procecor_AMD = input('Masukkan jenis procecor_AMD RYZEN (3/5/7/9): ')
layar = input('Masukkan jenis layar (TN/VA/IPS/OLED): ')
resolusi_layar = input('Masukkan resolusi layar (1024 x 768/ 1366 x 768/ 1920 x 1080): ')
berat = input('Masukkan berat dalam satuan kg (1/2): ')

# membuat objek laptop dengan spesifikasi yang dimasukkan oleh user
laptop = Komputer(memori, ram, procesor_Intel,procecor_AMD,layar, resolusi_layar, berat)

# menghitung harga laptop
harga_laptop = laptop.hitung_harga()

# menyimpan harga laptop ke file
with open('harga_laptop.txt', 'w') as f:
  f.write(str(harga_laptop))

# menampilkan harga laptop ke layar
print(f'Harga laptop: {harga_laptop}')

# menampilkan nama file yang telah disimpan
print(os.path.abspath('harga_laptop.txt'))
