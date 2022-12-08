def KoversiSuhu(C=0, F=0):
    """Membuat program yang dapat menkonversi suhu
    satuan celcius dan fahrenheit"""
    Cel=(5/9*(F-32))
    Fah=((9/5*C)+32)
    if C==0:
        print("Suhu",F,"Fahrenheit setara dengan",int(Cel),"Celcius")
    else:
        print("Suhu",C,"Fahrenheit setara dengan",int(Fah),"Fahrenheit")
print(KoversiSuhu(9))
print(KoversiSuhu(89))