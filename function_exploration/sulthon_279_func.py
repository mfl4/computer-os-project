# def luas_jajargenjang(a, t):
#      """mengembalikan luas jajar genjang"""
#      L= a*t
#      return L
# print(luas_jajargenjang(12,100))

print(" ———Toko UMMI———")
def sumof(price,summ):
     """fungsi untuk menghitung Total bayar"""
     return Price*summ
#input data
Price= int(input("masukan harga barang: "))
summ= int(input("masukan jumlah baju yang dibeli: "))
sumfor=sumof(Price,summ)

#diskon 5% tiap pembelian di atas Rp.100rb
if summ>100000:
     summ=summ-0.05*summ
print("Total Harga = ", "Rp.",summ)
Pay=int(input("Jumlah Nominal Uang =" ))
Retrn= (Pay-summ)
print("Uang Kembalian = ", "Rp.",Retrn)

