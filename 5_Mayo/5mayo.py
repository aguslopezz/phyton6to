import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import pandas as pd

df1 = pd.read_csv("./dnrpa-transferencias-autos-202204.csv")
df1 = df1.loc[0:130086]
x_values = df1['titular_genero'].unique()
y_values = df1['titular_genero'].value_counts().tolist()

# gráfico 1
plt1.bar(x_values, y_values)
plt1.title('titulares de autos')
plt1.xlabel('pais')
plt1.ylabel('cantidad de autos')
plt1.show()
