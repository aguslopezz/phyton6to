
boolean = True
dict = {}
i = 0

while i == 0:
    int = input("Ingrese 0 para terminar..  ")

    if int == "0":
        break
    
    else:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        dict[nombre] = edad

print(dict)