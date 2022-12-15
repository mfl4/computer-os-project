class PersegiPanjang(object): 
    def __init__(self,panjang,lebar):
        self.pjg=panjang 
        self.lbr=lebar
    pass

    def luas(self):
        """mengembalikan luas Persegi Panjang ini"""
        return self.pjg* self.lbr
PersegiPanjang1 = PersegiPanjang (7,9)
print("luas Persegi Panjang adalah    : ",PersegiPanjang1.luas())