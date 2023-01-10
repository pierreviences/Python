class Hero:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " Menyerang " + lawan.name)
        # Hero.diserang(lawan)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack):
        print(self.name + " diserang " + lawan.name)
        attack_diterima = attack/self.armor
        print("Serangan terasa : " + str(attack_diterima))
        self.health -= attack_diterima
        print("Darah " + self.name + " tersisa " + str(self.health))


sasuke = Hero("sasuke", 100, 10, 5)
naruto = Hero("Naruto", 100, 20, 10)

sasuke.serang(naruto)
print()
naruto.serang(sasuke)
