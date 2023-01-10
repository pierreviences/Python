import numpy as np
# untuk matematika -> lebih ke matrix

vector_a = np.array([1, 2, 3, 4])

# bisa langsung di kuadratin, dikali, dll, berbeda dengan list
print(vector_a**2)
print(vector_a*5)


matrix_b = np.array([(1, 2), (3, 4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((2, 2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2, 2))
print(f"ones c = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")
