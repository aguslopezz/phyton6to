import csv
import cv2
from pathlib import Path

#csv1
ids = []
nombres = []
numRostros = []

#csv2
idsOne = []
nombresOne = []
posicionOne = []

clasificador_de_rostros = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

for i, img_path in enumerate(Path("/content/sample_data/fotos").glob("*.jpg")):
  current = cv2.imread(str(img_path))
  copia_imagen = current.copy()
  rostros = clasificador_de_rostros.detectMultiScale(current)

  #csv1
  ids.append(i)
  nombres.append(img_path.stem)
  numRostros.append(len(rostros))

  for(x,y,ancho,alto) in rostros:
    cv2.rectangle(current,(x,y),(x+ancho,y+alto),(0,255,255),2)
    rostro = copia_imagen[y:y+alto,x:x+ancho]
    cv2.imwrite('rostro'+str(i)+'.jpg',rostro)

    #csv2
    idsOne.append(i)
    nombresOne.append('rostro'+str(i)+'.jpg')
    posicionOne.append([x,y])



with open('csv1.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  for n, name in enumerate(nombres):
    writer.writerow([ids[n], name, numRostros[n]])


with open('csv2.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  for n, name in enumerate(nombresOne):
    writer.writerow([idsOne[n], name, posicionOne[n]])