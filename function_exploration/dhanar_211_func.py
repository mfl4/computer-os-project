def kecepatan(Kmj):
    """Menghitung Kecepatan dari Kilometer per jam kedalam Meter per detik"""
    detik = 3600 #1 jam adalah 3600 detik
    meter = 1000 #1 kilometer adalah 1000 Meter
    return Kmj * meter / detik

Kc = kecepatan(360)
print("Jadi hasilnya adalah",Kc,"Meter/Detik")

def rupiah(Rp):
    """Menghitung Nilai Rupiah kedalam Dollar Amerika"""
    dollar = 15600 #1 dollar sama dengan Rp15600,-
    return Rp / dollar

Rp = rupiah(230000)
print("Jadi Hasilnya adalah",Rp,"Dollar")