import pandas as pd
import matplotlib.pyplot as plt

nombres = pd.read_csv("/content/nombres-2010-2014.csv",sep=",",engine="python")
actividades = pd.read_csv("/content/actividades-culturales-2021.csv",sep=";",engine="python")

condicion = actividades.Modalidad == "Virtual"
print("Actividades virtuales")
print(actividades[['Modalidad']][condicion].count())

print("Actividades presenciales")
condicion = actividades.Modalidad == "Presencial"
print(actividades[['Modalidad']][condicion].count())

plt.rcParams["figure.figsize"] = [17.0, 8.0]
x_values = actividades['Modalidad'].unique()
y_values = actividades['Modalidad'].value_counts(sort=False).tolist()
 
colores = ["#F2602B","#009999","#FFFF44", "#FF9933"]
p1 = plt.bar(x_values, y_values, color=colores)
plt.title('Modalidad de las actividades')
plt.xlabel('Modalidad')
plt.ylabel('Cantidad')
plt.show()

condicion = actividades.se_suspende_por_lluvia != "No"
print(actividades[['se_suspende_por_lluvia']][condicion].count())

condicion = (actividades.fecha_inicio >= "2021-05-01") & (actividades.fecha_fin <= "2021-05-30")
print(actividades[['fecha_inicio']][condicion])

condicion = (actividades.se_suspende_por_lluvia != "No") & (actividades.fecha_inicio >= "2021-09-01") & (actividades.fecha_fin <= "2021-09-30")
print(actividades[['actividad']][condicion].count())

condicion = (actividades.descripcion_actividad.str.contains('cine')) & (actividades.descripcion_actividad != "nan")
print(actividades[['actividad']][condicion])

print(actividades.groupby(['barrio']).count())

condicion = (actividades.descripcion_actividad.str.contains('musica')) & (actividades.barrio == "VILLA URQUIZA")
print(actividades[['actividad']][condicion].count())


condicion = nombres.anio == 2012
print(nombres[['nombre']][condicion].count())

condicion = (nombres.anio == 2012) & (nombres.nombre.str.startswith('S'))
print(nombres[['nombre']][condicion].count())

condicion = (nombres.nombre.str.startswith('A')) | (nombres.nombre.str.startswith('E')) | (nombres.nombre.str.startswith('I')) | (nombres.nombre.str.startswith('O')) | (nombres.nombre.str.startswith('U'))
print(nombres[['nombre']][condicion].count())

condicion = (nombres.nombre.str.startswith('A')) | (nombres.nombre.str.startswith('E')) | (nombres.nombre.str.startswith('I')) | (nombres.nombre.str.startswith('O')) | (nombres.nombre.str.startswith('U'))
nombresVocal = nombres[['nombre']][condicion]

condicion = (nombres.anio >= 2010) & (nombres.anio <= 2013)
print(nombresVocal[['nombre']][condicion].count())

numero = nombres.cantidad.max()
condicion = nombres.cantidad == numero
print(nombres[['nombre']][condicion])

condicion = nombres.anio == 2014
anio2014 = nombres[condicion]

numero = anio2014.cantidad.max()
condicion = anio2014.cantidad == numero
print(anio2014[['nombre']][condicion])

condicion = nombres.anio == 2010
anio2010 = nombres[condicion]

numero = anio2010.cantidad.min()
condicion = anio2010.cantidad == numero
print(anio2010[['nombre']][condicion])

condicion = (nombres.anio == 2011) & (nombres.nombre.str.startswith('A'))
anio2011 = nombres[condicion]

numero = anio2011.cantidad.min()
condicion = anio2011.cantidad == numero
print(anio2011[['nombre']][condicion])

print(nombres.cantidad.mean())

print(nombresUsados / nombresTotales[['nombre']])

condicion = nombres.anio == 2010
anio = nombres[condicion]

print("Promedio de nombres distintos usados en el 2010")
print(anio.cantidad.mean())

condicion = nombres.anio == 2011
anio = nombres[condicion]

print("Promedio de nombres distintos usados en el 2011")
print(anio.cantidad.mean())

condicion = nombres.anio == 2012
anio = nombres[condicion]

print("Promedio de nombres distintos usados en el 2012")
print(anio.cantidad.mean())

condicion = nombres.anio == 2013
anio = nombres[condicion]

print("Promedio de nombres distintos usados en el 2013")
print(anio.cantidad.mean())


condicion = nombres.anio == 2014
anio = nombres[condicion]

print("Promedio de nombres distintos usados en el 2014")
print(anio.cantidad.mean())

nombresUnicos = nombres.nombre.drop_duplicates()
print(nombresUnicos.count())

condicion = nombres.nombre.str.startswith('A')
print("Cantidad de nombres que empiezan con A")
print(nombres[['nombre']][condicion].count())

condicion = nombres.nombre.str.startswith('E')
print("Cantidad de nombres que empiezan con E")
print(nombres[['nombre']][condicion].count())

condicion = nombres.nombre.str.startswith('I')
print("Cantidad de nombres que empiezan con I")
print(nombres[['nombre']][condicion].count())

condicion = nombres.nombre.str.startswith('O')
print("Cantidad de nombres que empiezan con O")
print(nombres[['nombre']][condicion].count())

condicion = nombres.nombre.str.startswith('U')
print("Cantidad de nombres que empiezan con U")
print(nombres[['nombre']][condicion].count())