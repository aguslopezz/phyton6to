import requests
import pandas as pd
from bs4 import BeautifulSoup

if __name__ == '__main__':

    pagina = requests.get("https://www.mercadolibre.com.ar/")
    print("codigo: ",pagina.status_code)
    print("contenido: ",pagina.content)

    objeto_sopa = BeautifulSoup(pagina.content, 'html.parser')
    print(objeto_sopa.prettify())
    print(objeto_sopa.children)
    listaDeObjetos = list(objeto_sopa.children)

    e1 = objeto_sopa.find_all('div', class_='home')
    e2 = objeto_sopa.find_all(class_="andes-carousel-snapped__pagination-item")
    e3 = objeto_sopa.find_all(id="_hjSafeContext_12700865")
    print(e1)
 

    f1 = objeto_sopa.select("div p")
    f2 = objeto_sopa.select("p.valor-de-clase")
    f3 = objeto_sopa.select("p#valor-de-id")

    g = f1[0]
    print(g)
    print("texto del párrafo: ",g.get_text())

  

    tag = objeto_sopa.find(class_="nav-menu")
    tag = tag.get_text()
    j = str(tag).split("\n")
    print(j)

    tag = objeto_sopa.find("p")
    tag = tag.get_text()
    k = str(tag).split("\n")
    print(k)

    objeto_sopa.find_all('p')
    objeto_sopa.find('p')
    objeto_sopa.find_all(class_="home")
    objeto_sopa.find_all('p', class_='home')
    objeto_sopa.find_all(id="_hjSafeContext_12700865")
    
    # Forma de crear un data frame a partir de un diccionario
    diccionario = {  'Weight': [23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71],
                       'Name': [23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71],
                       'patas':[23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71],
                        'Age': [23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71,23, 88, 56, 15, 71],
                  }
    df = pd.DataFrame.from_dict(diccionario, orient='index')

    dataframe = pd.DataFrame(diccionario)
    dataframe.to_csv("nuevo_dataset.csv")
