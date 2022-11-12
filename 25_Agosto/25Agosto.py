from typing_extensions import Self
import cv2
import requests
import os
import pandas
import pathlib
import pandas as pd
#df = pd.read_csv("/content/diario_impreso.csv")

diccionario = {      'categoria':['Cantidad total de registros', 'CABA','PBA','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La pampa','La rioja','Mendoza','Misiones','Rio negro','Salta','San juan','San luis','Santa cruz','Santa fe','Santiago del estero','Tierra del fuego','Tucumán'],
                       'categoria':['Cantidad total de registros', 'CABA','PBA','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La pampa','La rioja','Mendoza','Misiones','Rio negro','Salta','San juan','San luis','Santa cruz','Santa fe','Santiagodel estero','Tierradel fuego','Tucumán'],
                       'categoria':['Cantidad total de registros', 'CABA','PBA','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La pampa','La rioja','Mendoza','Misiones','Rio negro','Salta','San juan','San luis','Santa cruz','Santa fe','Santiagodel estero','Tierradel fuego','Tucumán'],
                        'categoria':['Cantidad total de registros', 'CABA','PBA','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La pampa','La rioja','Mendoza','Misiones','Rio negro','Salta','San juan','San luis','Santa cruz','Santa fe','Santiagodel estero','Tierradel fuego','Tucumán'],
                      }
df = pd.DataFrame.from_dict(diccionario, orient='index')

dataframe = pd.DataFrame(diccionario)
dataframe.to_csv("nuevo_dataset.csv")
#df = pd.DataFrame([[0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4], [0,4, 4, 1,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4], [10,4, 20, 30,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4],[0,4, 4, 1,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4,0, 2, 3,4]],
                  #index=['Cantidad total de registros', 'CABA','PBA','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La pampa','La rioja','Mendoza','Misiones','Rio negro','Salta','San juan','San luis','Santa cruz','Santa fe','Santiago del estero','Tierra del fuego','Tucumán'
                        #], columns=['Categoría','Diarios', 'Editoriales', 'Salas de cine'])
