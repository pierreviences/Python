# module matematika dengan import

from matematika import tambah  # ngambil cuman 1
from matematika import *  # ngambil semuanya

hasil_tambah = tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")


hasil_kali = kali(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"Hasil Pangkat 3 = {pangkat_3(3)}")
