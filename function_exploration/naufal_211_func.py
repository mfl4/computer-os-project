def Koversi_Suhu(C=0, F=0):
    """Membuat program yang dapat menkonversi suhu
    satuan celcius dan fahrenheit"""
    Cel=(5/9*(F-32))
    Fah=((9/5*C)+32)
    if C==0:
        print("Suhu",F,"Fahrenheit setara dengan",int(Cel),"Celcius")
    else:
        print("Suhu",C,"Celcius setara dengan",int(Fah),"Fahrenheit")
Koversi_Suhu(C=9)
Koversi_Suhu(F=89)
