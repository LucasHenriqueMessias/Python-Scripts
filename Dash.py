import dash
import plotly
#é possivel utilizar o openpyxl pra transportar as informações para o dataframe, e utilizar como dashboard
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

#definindo a base de dados como dataframe de um json com array
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
#Criando o gráfico
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

#layout, o que será exibido
app.layout = html.Div(children=[ #cria um div para layout em formato de lista de itens
    html.H1(children='Hello Dash'), #cria um h1 (titulo) com a informação hello dash

    html.Div(children=''' 
        Dash: A web application framework for your data. 
    '''), #cria um div para passar o texto 

    dcc.Graph( #inclui o gráfico do dashboard no html para exibição
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)