import plotly.express as px
import pandas as pd

data = {'Artista': ['Gorillaz', 'Red Hot Chili Peppers'],
        'Reproducciones': [1040234854, 1055738398]}
df = pd.DataFrame(data)

fig = px.bar(df, x='Artista', y='Reproducciones', title='Reproducciones de YouTube por Artista')

fig.show()
