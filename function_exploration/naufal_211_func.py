def koversi_suhu(C=0, F=0):
    """Membuat program yang dapat menkonversi suhu
    satuan celcius dan fahrenheit"""
    Cel=(5/9*(F-32))
    Fah=((9/5*C)+32)
    if C==0:
        print("Suhu",F,"Fahrenheit setara dengan",int(Cel),"Celcius")
    else:
        print("Suhu",C,"Celcius setara dengan",int(Fah),"Fahrenheit")
koversi_suhu(C=9)
koversi_suhu(F=89)
