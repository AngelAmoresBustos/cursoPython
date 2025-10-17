miLista = ["manzana", "banana", "cereza"]
print(miLista)

miLista.append("naranja")   
print(miLista)

miLista.insert(2,"fresa")   
print(miLista)

miLista.extend(["kiwi", "mango"])   
print(miLista)

print(miLista.index("banana"))
print(miLista)

print(miLista[0:1])
print(miLista[:2])
print(miLista[2:])

print("banana" in miLista)

miLista.remove("banana")
print(miLista)
print(miLista.pop())