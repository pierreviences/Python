class Hero:
    jumlah_hero = 0

    def __init__(self, name, umur):
        self.name = name
        self.umur = umur
        Hero.jumlah_hero += 1

    # void function, method tanpa return
    def siapa(self):
        print("Namaku adalah " + self.name)

    # method dengan argumen
    def umurUp(self, up):
        self.umur += up

    # method dengan return
    def getUmur(self):
        return self.umur


hero1 = Hero("Yazid", 20)
print(hero1.__dict__)

hero1.siapa()
hero1.umurUp(10)
print(hero1.umur)

print(hero1.getUmur())
