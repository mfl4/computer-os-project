def barisan_aritmatika(a=0,u2=0,u1=0,n=0):
    """Membuat penyelesaian dari barisan aritmatika """
    b = int(u2 - u1)
    Un = str(input("Masukan suku :"))
    if True:
        r =(a + ((n-1) * b))
        print("Suku ke " + Un + " Adalah " + str(r))

#note jika ingin mengubah a/u2/u1/n tinggal mengubah sesuai urutannya
#contoh soal 1
#Ada suatu barisan aritmatika dengan pola 5,8,11.... Maka berapa suku ke 24?
barisan_aritmatika(5,8,5,24)
#contoh soal 2
# Ada suatu barisan aritmatika 14,23,52.... Maka berapa suku ke 128?
barisan_aritmatika(14,23,14,128)
