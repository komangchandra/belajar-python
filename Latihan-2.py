# Tipe Data

# Tipe data angka
data_integer = 5 #ini adalah integer
print("angka: ", data_integer)
print("-bertipe:", type(data_integer))

data_float = 5.4 #ini adalah float
print("angka: ", data_float)
print("-bertipe:", type(data_float))

# Tipe sata string
data_sting = "Komang Chandra" #string
print("tulisan: ", data_sting)
print("-bertipe:", type(data_sting))

# Tipe data boolean
data_boolean1 = False
data_boolean2 = True
print("data: ", data_boolean1, "&", data_boolean2)
print("-bertipe:", type(data_boolean1))

# Tipe data bilangan complex
data_complex = complex(5,6)
print("data: ", data_complex)
print("-bertipe:", type(data_complex))

# kita bisa menggunakan type data dari bahasa C
from ctypes import c_double #mengimport dari librari C

data_c_double = c_double(10.5)
print("data: ", data_c_double)
print("-bertipe:", type(data_c_double))