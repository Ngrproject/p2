print("\t\t APLIKASI KASIR PINTAR")
print("=======================================================")
totbel=float(input("MASUKAN TOTAL BELANJA\t:"))
if totbel >= 500000:
    discount=0.2*totbel
    bayar=totbel-discount
elif totbel >= 300000:
    discount=0.15*totbel
    bayar=totbel-discount
elif totbel >= 100000:
    discount=0.1*totbel
    bayar=totbel-discount
else: discount=0
bayar=totbel-discount

if bayar >= 500000:
    hadiah ="Selamat..... Anda mendapatkan Innova Reborn Diesel"
elif bayar >= 300000:
    hadiah ="Selamat..... Anda mendapatkan Toyota Avanza"
elif bayar >= 100000:
    hadiah ="Selamat..... Anda mendapatkan Honda Beat"
else:
    hadiah ="Maaff..... Anda mendapatkan Hikmahnya"
print("=======================================================")
print("Pembelian\t\t:" ,totbel)
print("Diskon\t\t\t:",discount)
print("Total Pembayaran\t:",bayar)
print("=======================================================")
print("Hadiah\t\t\t:",hadiah)




