from cmath import log
import requests


if __name__ == '__main__':

    archivo = open("datos.csv", "w")
    nombres_columnas = "actividad , tipo , precio \n"
    archivo.write(nombres_columnas)
    archivo.close()
    
    for i in range(30):
        respuesta = requests.get('https://www.boredapi.com/api/activity')
        respuesta.status_code
        informacion = respuesta.json()
        actividad = informacion["activity"]
        tipo = informacion["type"]
        precio = str(informacion["price"])

        linea = actividad + " , " + tipo + " , " + precio + "\n"

        archivo = open("datos.csv", "a")
        archivo.write(linea)
        archivo.close()