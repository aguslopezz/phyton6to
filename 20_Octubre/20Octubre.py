from folium import Map,Marker,IFrame,Popup
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/oferta_gastronomica.csv')

ubicacion_de_buenos_aires = [-34.603722, -58.381592]

mapa = Map(location=ubicacion_de_buenos_aires, zoom_start=12,tooltip = 'This tooltip will appear on hover')

for i, longitud in enumerate(df["long"]):  
    latitud = df["lat"][i]
    html1 = f'''Nombre: {df["nombre"][i].replace("`", "'")} <br>Comidas: {df["cocina"][i]}'''
    html2 = f'''<p>Direccion: {df["direccion_completa"][i]}<br>Telefono: {df["telefono"][i]}<br>Barrio:{df["barrio"][i]}<p/>'''

    iframe = IFrame(html2,
                       width=100,
                       height=100)
    popup = Popup(iframe,
                     max_width=100)    
       
    marcador = Marker( location=[latitud,longitud],
                      popup=popup,
                      tooltip=html1)
    mapa.add_child(marcador)
mapa.save('mapa_con_ubicaciones.html')