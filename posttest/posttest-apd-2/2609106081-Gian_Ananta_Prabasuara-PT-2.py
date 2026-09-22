komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

harga_komponen = [komponen_1, komponen_2, komponen_3,komponen_4, komponen_5, komponen_6,]

total_biaya = harga_komponen [0] + harga_komponen [1] + harga_komponen [2] + harga_komponen [3] + harga_komponen [4] + harga_komponen [5]

rata_rata = total_biaya / len(harga_komponen)

nim = 81
bolean = nim != rata_rata

GBP = 23820.31
total_biaya_poundsterling = total_biaya / GBP

komponen_1_sampai_4 = harga_komponen[-6:-2]

print("Komponen 1: Rp", komponen_1)
print("Komponen 2: Rp", komponen_2)
print("Komponen 3: Rp", komponen_3)
print("Komponen 4: Rp", komponen_4)
print("Komponen 5: Rp", komponen_5)
print("Komponen 6: Rp", komponen_6)

print("Total Biaya: Rp", total_biaya)
print("Rata-rata: Rp", rata_rata)
print("NIM: ", nim)
print("Bolean:", bolean)
print("1 Poundsterling: Rp", GBP)
print("Total Biaya dalam Poundsterling: £", total_biaya_poundsterling)
print("Komponen 1 sampai 4: ", komponen_1_sampai_4)
