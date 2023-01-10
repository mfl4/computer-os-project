import os

class Computer:
# inisiasi
    def __init__(self, vga, ram, procesor_Intel, procesor_AMD, mobo_intel, mobo_amd, psu,cooling):
    #, harga, ukuran_layar, port_usb, hdmi, wifi, durasi_baterai, , dimensi, merek, sistem_operasi, kamera, speaker
        self.vga = vga
        self.ram = ram
        self.procesor_Intel = procesor_Intel
        self.procesor_AMD = procesor_AMD
        self.mobo_intel = mobo_intel
        self.mobo_amd = mobo_amd
        self.psu = psu
        self.cooling = cooling
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
    def sum_price(self):
        total_price = 0

        # Memori
        if self.vga == 'GTX 1050':
            total_price += 2250000
        elif self.vga == 'GTX 1050 TI':
            total_price += 2775000
        elif self.vga == 'GTX 1650':
            total_price += 3215000
        elif self.vga == 'GTX 1660 ':
            total_price += 3550000
        elif self.vga == 'GTX 1660 SUPER':
            total_price += 3760000
        elif self.vga == 'GTX 1660 TI':
            total_price += 3950000
        elif self.vga == 'RTX 2060':
            total_price += 4200000
        elif self.vga == 'RTX 2060 SUPER':
            total_price += 4855000
        elif self.vga == 'RTX 2070':
            total_price += 5650000
        elif self.vga == 'RTX 2070 SUPER':
            total_price += 6230000
        elif self.vga == 'RTX 2080':
            total_price += 6850000
        elif self.vga == 'RTX 2080 SUPER':
            total_price += 8215000
        elif self.vga == 'RTX 2080 TI':
            total_price += 9250000
        elif self.vga == 'RTX 3060':
            total_price += 6550000
        elif self.vga == 'RTX 3060 TI':
            total_price += 7210000
        elif self.vga == 'RTX 3070':
            total_price += 7850000
        elif self.vga == 'RTX 3070 TI':
            total_price += 8210000
        elif self.vga == 'RTX 3080':
            total_price += 9650000
        elif self.vga == 'RTX 3080 TI':
            total_price += 1159000
        elif self.vga == 'RTX 3090':
            total_price += 1525000
        elif self.vga == 'RTX 3090 TI':
            total_price += 1875000
        else:
            total_price += 0

        # Ram
        if self.ram == '8 GB':
            total_price += 650000
        elif self.ram == '16 GB':
            total_price += 1200000
        elif self.ram == '32 GB':
            total_price += 2250000
        elif self.ram == '64 GB':
            total_price += 4220000
        else:
            total_price += 0

        # Procesor Intel
        if self.procesor_Intel == 'i3 10100':
            total_price += 1350000
        elif self.procesor_Intel == 'i5 10400':
            total_price += 1900000
        elif self.procesor_Intel == 'i5 10600k':
            total_price += 3300000
        elif self.procesor_Intel == 'i7 10700':
            total_price += 3200000
        elif self.procesor_Intel == 'i7 10700k':
            total_price += 4600000
        elif self.procesor_Intel == 'i9 10900':
            total_price += 5400000
        elif self.procesor_Intel == 'i7 10900k':
            total_price += 6000000
        elif self.procesor_Intel == 'i3 11100':
            total_price += 1350000
        elif self.procesor_Intel == 'i5 11400':
            total_price += 2200000
        elif self.procesor_Intel == 'i5 11600k':
            total_price += 3450000
        elif self.procesor_Intel == 'i7 11700':
            total_price += 3850000
        elif self.procesor_Intel == 'i7 11700k':
            total_price += 5100000
        elif self.procesor_Intel == 'i9 11900':
            total_price += 6200000
        elif self.procesor_Intel == 'i9 11900k':
            total_price += 7350000
        elif self.procesor_Intel == 'i3 12100':
            total_price += 2100000
        elif self.procesor_Intel == 'i5 12400':
            total_price += 2700000
        elif self.procesor_Intel == 'i5 12600k':
            total_price += 4900000
        elif self.procesor_Intel == 'i7 12700':
            total_price += 5700000
        elif self.procesor_Intel == 'i7 12700k':
            total_price += 7650000
        elif self.procesor_Intel == 'i9 12900':
            total_price += 8250000
        elif self.procesor_Intel == 'i9 12900k':
            total_price += 9200000
        elif self.procesor_Intel == 'i3 13100':
            total_price += 2500000
        elif self.procesor_Intel == 'i5 13400':
            total_price += 3750000
        elif self.procesor_Intel == 'i5 13600k':
            total_price += 5250000
        elif self.procesor_Intel == 'i7 13700':
            total_price += 6500000
        elif self.procesor_Intel == 'i7 13700k':
            total_price += 8240000
        elif self.procesor_Intel == 'i9 13900':
            total_price += 9400000
        elif self.procesor_Intel == 'i9 13900k':
            total_price += 1055000

        # procesor Amd
        elif self.procesor_AMD == '5 3600x':
            total_price += 2200000
        elif self.procesor_AMD == '7 3800x':
            total_price += 3150000
        elif self.procesor_AMD == '9 3900x':
            total_price += 5240000
        elif self.procesor_AMD == '9 3950x':
            total_price += 7200000
        elif self.procesor_AMD == '5 5600':
            total_price += 2100000
        elif self.procesor_AMD == '5 5600x':
            total_price += 2450000
        elif self.procesor_AMD == '7 5700x':
            total_price += 3325000
        elif self.procesor_AMD == '7 5800x':
            total_price += 4100000
        elif self.procesor_AMD == '9 5900x':
            total_price += 6200000
        elif self.procesor_AMD == '9 5950x':
            total_price += 8250000
        elif self.procesor_AMD == '5 7600x':
            total_price += 4850000
        elif self.procesor_AMD == '7 7800x':
            total_price += 7250000
        elif self.procesor_AMD == '9 7900x':
            total_price += 8900000
        elif self.procesor_AMD == '9 7950x':
            total_price += 9950000
        else:
            total_price += 0

        # motherboard Intel
        if self.mobo_intel == 'B460':
            total_price += 3250000
        elif self.mobo_intel == 'B560':
            total_price += 4525000
        elif self.mobo_intel == 'B660':
            total_price += 5750000
        elif self.mobo_intel == 'Z490':
            total_price += 10525000
        elif self.mobo_intel == 'Z590':
            total_price += 17560000
        elif self.mobo_intel == 'Z690':
            total_price += 25520000

        #motherboard AMD
        elif self.mobo_amd == 'B450':
            total_price += 2340000
        elif self.mobo_amd == 'B550':
            total_price += 4525000
        elif self.mobo_amd == 'B650':
            total_price += 5250000
        elif self.mobo_amd == 'X470':
            total_price += 5152000
        elif self.mobo_amd == 'X570':
            total_price += 8925000
        elif self.mobo_amd == 'X670':
            total_price += 1525000
        else:
            total_price += 0
            
        # power supply
        if self.psu == '400w':
            total_price += 650000
        elif self.psu == '450w':
            total_price += 725000
        elif self.psu == '500w':
            total_price += 820000
        elif self.psu == '550w':
            total_price += 865000
        elif self.psu == '600w':
            total_price += 885000
        elif self.psu == '800w':
            total_price += 1250000
        elif self.psu == '1200w':
            total_price += 1625000
        else:
            total_price += 0
        
        # cooling menggunak All in one, tidak menerima cooling konvensional
        if self.cooling == '120':
            total_price += 1250000
        elif self.cooling == '240':
            total_price += 2340000
        elif self.cooling == '360':
            total_price += 4525000
        else:
            total_price += 0
            
        # mengembalikan nilai total_price
        return total_price

# # meminta input spesifikasi laptop dari user
# memori = input('Masukkan jenis memori (512/1000)GB: ')
# ram = input('Masukkan jumlah RAM (4/6/8/16)GB: ')
# procesor_Intel = input('''Masukkan jenis procesor_Intel |  i3 10100  |   i5 10400    |   i7 10700    |   i9 10900    |   i5 10600k   |   i7 10700k   |   i9 10900k   |
#                               |  i3 11100  |   i5 11400    |   i7 11700    |   i9 11900    |   i5 11600k   |   i7 11700k   |   i9 11900k   |
#                               |  i3 12100  |   i5 12400    |   i7 12700    |   i9 12900    |   i5 12600k   |   i7 12700k   |   i9 12900k   |
#                               |  i3 13100  |   i5 13400    |   i7 13700    |   i9 13900    |   i5 13600k   |   i7 13700k   |   i9 13900k   |
#                                                                                                                         Processor yang dipilih  :''')
# procecor_AMD = input('''Masukkan jenis procecor_AMD RYZEN |  5 3600x  |  7 3800x  |  9 3900x  |  9 3950x  |
#                                   |  5 5600x  |  7 5800x  |  9 5900x  |  9 5950x  |
#                                   |  5 7600x  |  7 7800x  |  9 7900x  |  9 7950x  |
#                                                               Processor yang dipilih  : ''')
# layar = input('Masukkan jenis layar (TN/VA/IPS/OLED): ')
# resolusi_layar = input('Masukkan resolusi layar (1024 x 768/ 1366 x 768/ 1920 x 1080): ')
# berat = input('Masukkan berat dalam satuan kg (1/2): ')

# # membuat objek laptop dengan spesifikasi yang dimasukkan oleh user
# harga_laptop = Computer(memori, ram, procesor_Intel,procecor_AMD,layar, resolusi_layar, berat,procesor_Intel)
# # menyimpan harga laptop ke file
# with open('harga_laptop.txt', 'w') as f:
#   f.write(str(harga_laptop))

# # menampilkan harga laptop ke layar
# print(f'Harga laptop: {harga_laptop}')

# # menampilkan nama file yang telah disimpan
# print(os.path.abspath('harga_laptop.txt'))


# data= ['i3 10100', 'i3 10100', 'i5 10400', 'i7 10700', 'i9 10900', 'i5 10600k' , 'i7 10700k' , 'i9 10900k',  'i3 11100', 'i5 11400', 'i7 11700', 'i9 11900', 'i5 11600k' , 'i7 11700k' , 'i9 11900k',  'i3 12100', 'i5 12400', 'i7 12700', 'i9 12900', 'i5 12600k' , 'i7 12700k' , 'i9 12900k',  'i3 13100', 'i5 13400', 'i7 13700', 'i9 13900', 'i5 13600k' , 'i7 13700k' , 'i9 13900k']

# for d in data:
#     print (f"Intel Core {d}")