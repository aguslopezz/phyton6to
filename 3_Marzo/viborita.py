from pickle import FALSE
from random import randrange


mapa = []
viborita = [[0,0],[1,0],[2,0],[3,0]]
cabeza = [3,0]
pos_modif = [0,0]
comida = [0,0]
comida[0] = randrange(0,10)
comida[1] = randrange(1,10)

puntos = 0

sigue = True
comio = False

def mostrarMapa():
    for i in mapa:
        print(i)


for i in range(0,11):
    mapa.append(["_","_","_","_","_","_","_","_","_","_"])

for i in range(0,4):
    mapa[0][i] = "0"

mapa[comida[1]][comida[0]] = "C"

while sigue:
    mostrarMapa()
    print(" ")
    print(f"Puntos: {puntos}")

    comio = False
    
    tecla = input()

    pos_modif[0] = cabeza[0]
    pos_modif[1] = cabeza[1]

    if tecla == 'w':
        cabeza[1] -= 1 
    elif tecla == 'a':
        cabeza[0] -= 1
    elif tecla == 's':
        cabeza[1] += 1
    elif tecla == 'd':
        cabeza[0] += 1

    viborita[3] = cabeza

    for i in range (2,-1,-1):
        pos_anterior = viborita[i]
        viborita[i] = pos_modif
        pos_modif = pos_anterior
        
    for y in range(0,10):
        for x in range(0,10):
            mapa[x][y] = "_"

    for i in viborita:
        x = i[0]
        y = i[1]
        mapa[y][x] = "0"

    if(cabeza == comida):
        puntos += 1
        comio = True

    if comio:
        comida[0] = randrange(0,10)
        comida[1] = randrange(0,10)
    
    mapa[comida[1]][comida[0]] = 'C'

    if(cabeza[0] < 0 or cabeza[0] > 9 or cabeza[1] < 0 or cabeza[1] > 9):
        sigue = False

print(f"Puntuación final: {puntos}")