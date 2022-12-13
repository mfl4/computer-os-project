#Deklarasi Fungsi
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4

    var_total = var_harian + var_uts + var_uas
    print(var_total)
fungsi_total_nilai(4,7,9)