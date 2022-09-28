dict = {"Mateo": 20, "Cala":40}

for i in dict:

    edad = dict.get(i)
    dict[i] = edad * 2

print(dict)