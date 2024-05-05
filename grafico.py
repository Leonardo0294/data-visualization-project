import pandas as pd
import plotly.express as px

# Paso 1: Cargar y Procesar los Datos desde el Archivo CSV
# Reemplaza 'ruta/a/tu/archivo.csv' con la ruta real donde se encuentra tu archivo CSV
df = pd.read_csv('./billboard.csv')

# Mostrar las primeras filas para verificar la carga de datos
print(df.head())

# Paso 2: Preparar y Filtrar los Datos para la Visualización
# Convertir la columna 'peak-rank' a tipo numérico
df['peak-rank'] = pd.to_numeric(df['peak-rank'], errors='coerce')

# Seleccionar las últimas 50 canciones (o menos si hay menos de 50 canciones)
df_last_50 = df.tail(50)

# Ordenar los datos por 'peak-rank' de forma ascendente
df_last_50 = df_last_50.sort_values(by='peak-rank', ascending=True)

# Paso 3: Crear el Gráfico de Barras Interactivo con Plotly Express
# Configurar y crear el gráfico de barras interactivo con Plotly Express
fig = px.bar(df_last_50, x='peak-rank', y='song', orientation='h',
             title='Peak Rank on Billboard Hot 100 (Last 50 Songs)',
             labels={'peak-rank': 'Peak Rank', 'song': 'Song'})

# Mostrar el gráfico interactivo
fig.show()
