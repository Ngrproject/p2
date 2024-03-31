print("program percabanagan 2 blok")
totbel=float(input("input total belanja"))
if totbel >= 250000:
    discount=0.1*totbel
    bayar=totbel-discount
else:
    discount=0
    bayar=totbel-discount

print("total belanja\t",totbel)
print("Discount\t",discount)
print("total bayar\t:",bayar)