list_kosong = []

while (True):
    no = 0
    print("\nMasukkan Data Film")
    film = input("Judul Film \t: ")
    aktor = input("Aktor Film \t: ")
    print()
    list_film = [film, aktor]
    list_kosong.append(list_film)
    print(10*"=", "DATA FILM", 10*"=")
    print("No ", "|", 3*" ", "Judul Film ", 3*" ", "|", " Aktor Film  ")
    for i in list_kosong:
        no += 1
        print(no, 1*" ", "|", 3*" ", i[0], 3*" ", "|", i[1])
    print("\n", 20*"=")
    lanjut = input("Apakah Dilanjutkan ? (y/n) : ")
    if (lanjut == "n"):
        break
