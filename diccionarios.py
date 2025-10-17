miDiccionario ={"Colombia":"Bogotá", "Perú":"Lima", "Chile":"Santiago", "Argentina":"Buenos Aires", "Ecuador":"Quito"}
print(miDiccionario)
print(miDiccionario["Colombia"])
miDiccionario["Venezuela"]="Caracas"
print(miDiccionario)
del miDiccionario["Ecuador"]
print(miDiccionario)

miTuplaPais = ("Colombia", "Peru", "Chile", "Argentina", "Ecuador")
miTuplaCapital = ("Bogota", "Lima", "Santiago", "Buenos Aires", "Quito")
miDiccionario2 = dict(zip(miTuplaPais, miTuplaCapital))
print(miDiccionario2)
print(miDiccionario2.keys())
print(miDiccionario2.values())