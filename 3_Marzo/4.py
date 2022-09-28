set1 = set()
set2 = set()

for i in range(0,3):
    nombre = input("Nombre: ")
    set1.add(nombre)

for i in set1:
    letra = i[0].lower()
    if letra != "a":
        set2.add(i)

set1 = set2

print(set1)