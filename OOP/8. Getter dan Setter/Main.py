class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    # jadi ini kita bikin function tapi seolah-olah ini tuh property/atribut
    # jadi pas kita panggil kita gak manggil seperti ini : object.info()
    # tapi kita manggil seperti ini : object.info
    def info(self):
        return f"name : {self.name} \nhealth: {self.__health}\n"

    # inisiasi buat bikin getter dan setter
    @property
    def armor(self):
        pass

    # untuk membuat getter
    # jadi pas kita panggil kita gak manggil seperti ini : object.armor()
    # tapi kita manggil seperti ini : object.armor
    @armor.getter
    def armor(self):
        return self.__armor

    # untuk membuat setter
    # jadi pas kita panggil kita gak manggil seperti ini : object.armor(20)
    # tapi kita manggil seperti ini : object.armor = nilai
    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delet')
        self.__armor = None


sniper = Hero('sniper', 100, 10)

print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)
