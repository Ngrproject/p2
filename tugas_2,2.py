print("\tAplikasi Penghitung Gaji Mingguan Karyawan")
print("\t\tPT Mencari Cinta Sejati.Tbk")
print("==========================================================")
Nama=(input("Nama Karyawan\t\t\t:"))
jamker=float(input("Input Jam Kerja\t\t\t:"))
Upah_Normal=4000
upah_lembur=5000
jam_min=48
if jamker <= 48:
   gp=jamker*Upah_Normal
   lembur=0
   jl=0
   gt=gp
elif jamker> 48:
    lembur=jamker-jam_min
    jl=lembur*upah_lembur
    gp=(jamker-lembur)*Upah_Normal
    gt=gp+jl

print("==========================================================")
print("Nama Karyawan\t\t\t:" ,Nama)
print("jumlah jam kerja\t\t:",jamker)
print("jumlah jam kerja Normal\t:",jam_min)
print("Jumlah Jam Lembur\t\t:",lembur)
print("==========================================================")
print("Gaji Pokok \t\t\t:",gp)
print("Gaji lembur \t\t\t:",jl)
print("==========================================================")
print("Gaji total \t\t\t:",gt)
