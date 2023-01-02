# Date and time latihan

import datetime as dt

hari = dt.date.today()
print(hari)
print(f"Hari ini adalah hari = {hari:%A}")

tanggal = dt.date(2003, 6, 23)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")


print("\n\nSilahkan masukkan tanggal,\nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan   : "))
tahun = int(input("Tahun   : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")


hari_ini = dt.date.today()
print(f"\nHari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
# .days -> buat ngambil harinya aja
umur_bulan = (umur_hari.days % 365) // 30
umur_tahun = umur_hari.days // 365
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan")
