class Hero:
    jumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        # tidak bisa diakses di luar class
        # underscorenya 2 __
        self.__private = "private"

        # variable instance protected
        # sama kaya public
        # underscorenya 1
        self._protected = "protected"


lina = Hero("lina", 100)
print(lina.__dict__)
