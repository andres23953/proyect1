import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('datos.csv')

# Eliminar duplicados
df = df.drop_duplicates()

# Agregaciones
suma = df['columna'].sum()
promedio = df['columna'].mean()

# Guardar el archivo limpio
df.to_csv('datos_limpios.csv', index=False)
