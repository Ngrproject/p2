print("program mengitung gaji")
print("======================================")
gapok=float(input("masukan gaji :"))
if gapok >= 5000000:
    pajak=0.1*gapok
    gaber=gapok-pajak
elif gapok >= 3000000:
    pajak=0.05*gapok
    gaber=gapok-pajak
elif gapok >= 2000000:
    pajak=0.01*gapok
    gaber=gapok-pajak
else:
    pajak=0
    gaber=gapok-pajak

print("========================================")
print("gaji pokok \t\t :" ,gapok)
print("pajak \t\t :" ,pajak)
print("========================================")
print("Gaji bersih anda\t:",gaber)
print("========================================")