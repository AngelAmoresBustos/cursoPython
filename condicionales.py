print("Programa de becas 2025")
distancia = int(input("¿Cuál es la distancia en km de su casa a la universidad? "))
print("Distancia: ", distancia, "km")
num_hermanos = int(input("¿Cuántos hermanos tienes? "))
print("Número de hermanos: ", num_hermanos)
salario_familiar = int(input("¿Cuál es el salario anual de su familia en euros? "))
print("Salario familiar: ", salario_familiar, "euros")

if distancia > 40 and num_hermanos > 2 or salario_familiar <= 20000:
    print("Usted puede optar a una beca")
else:
    print("Usted no puede optar a una beca")
    