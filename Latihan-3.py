# Casting Data
# merubah dari 1 tipe ke tipe lain
# Jenis tipe data bisa dilihat di latihan 2

print("====Dari Integer=====")
data_integer = 0 #ini adalah integer
print("angka: ", data_integer)
print("-bertipe:", type(data_integer))
# rubah integer ke float, string, dan boolean
data_float = float(data_integer)
data_string = str(data_integer)
data_boolean = bool(data_integer)
print("data", data_float, "-float:", type(data_float))
print("data", data_string, "-string:", type(data_string))
print("data", data_boolean, "-boolean:", type(data_boolean)) #nilai akan selalu true jika tidak 0

print("====Dari String=====")
data_string = "0"
# rubah String ke float, integer, dan boolean
data_float = float(data_string)
data_integer = int(data_string)
data_boolean = bool(data_string)
print("data", data_string, "-string:", type(data_integer))
print("data", data_float, "-float:", type(data_float))
print("data", data_boolean, "-boolean:", type(data_boolean)) #data yang memiliki nilai akan selalu menghasilkan True, kecuali variabl tidak memiliki data atau ""
# ketika nilai string bukan berupa angka, maka akan error, 