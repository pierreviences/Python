class Hero:  # templat class
    # class variabel
    jumlah = 0

    def __init__(self, nama, umur):
        # instance variabel
        self.nama = nama,
        self.umur = umur,

        # mengakses variabel
        Hero.jumlah += 1


hero1 = Hero("yazid", 19)
print(Hero.jumlah)

hero2 = Hero("yazid", 19)
print(Hero.jumlah)

hero3 = Hero("yazid", 19)
print(Hero.jumlah)
