# cara 1
import sains as s

# dari package sains
hasil_tambah = s.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil Tambah = {hasil_tambah}")

hasil_fisika = s.fisika.gaya(10, 9.8)
print(f"Hasil Tambah = {hasil_fisika}")

hasil_kali = s.kali(1, 2, 3, 4, 5)
print(f"Hasil Kali = {hasil_kali}")

# dari package sains -> mtk
hasil_add = s.mtk.basic.add(1, 2)
print(f"Hasil Tambah dari 2 package = {hasil_add}")

hasil_k = s.mtk.k(1, 2)
print(f"Hasil kali dari 2 package = {hasil_k}")


'''
# cara 2
from sains import *
# dari package sains
hasil_tambah = matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil Tambah = {hasil_tambah}")

hasil_fisika = fisika.gaya(10, 9.8)
print(f"Hasil Tambah = {hasil_fisika}")

# dari package sains -> mtk
hasil_add = mtk.basic.add(1, 2)
print(f"Hasil Tambah dari 2 package = {hasil_add}")
'''
