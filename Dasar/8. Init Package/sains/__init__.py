# cara 1
from . import matematika, fisika, mtk
from .matematika import kali

'''
# cara 2 -> dipake ketika * semua pas di import yang ada di file main dan dipake sama sama cara 2
__all__ = [
    "matematika",
    "fisika",
    "mtk"
]
'''
