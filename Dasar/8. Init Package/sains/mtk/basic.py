def add(*args):
    hasil = 0
    for data in args:
        hasil += data

    return hasil


def k(*args):
    hasil = 1
    for data in args:
        hasil *= data

    return hasil
