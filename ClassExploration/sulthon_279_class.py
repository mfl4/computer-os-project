#Class Exploration
#Dibuat Oleh Sulthon Kaffaah Al Farizzi
#NIM L200220279 

class manusia():
    
    ucap = " Mengucap sesuatu dalam bahasa Jawa "
    
    def __init__(self, nama):
        """ Fungsi ini menambahkan instance."""
        self.nama = nama 
         
    def tampilkan(self):
        """menampilkan percakapan antara 2 orang"""
        print("Farhan: Seseorang yang bernama"+ self.nama + "mengatakan sesuatu hal")
        print("Rizky: Apa yang dia katakan?")  
         
    def jawab(self):
        """Menampilkan balasan Farhan"""
        print("Fahan: Sepertinya "+ self.ucap + " Tapi nggak terlalu jelas ")   
        
             
farhan = manusia(" Yusuf Cahyo ")
print(farhan.tampilkan())
print(farhan.jawab())
