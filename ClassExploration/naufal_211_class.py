class PersegiPanjang(object): 
    """data dan proses terhadap persegi panjang dengan panjang(pjg) dan lebar(lbr)"""
    def __init__(self,panjang,lebar):
        self.pjg=panjang 
        self.lbr=lebar
        """mengisi property yang tidak punya nilai default"""
        pass #program diatas tidak ada yg dieksekusi dan langsung melanjutkan program dibawahnya.

    def luas(self):
        """mengembalikan luas Persegi Panjang ini"""
        return self.pjg* self.lbr
PersegiPanjang1 = PersegiPanjang (7,9)
print("luas Persegi Panjang adalah    : ",PersegiPanjang1.luas())
