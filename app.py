from data_generator import getData
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# print(getData())


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


with open('collection.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)


df['like']=df['like'].cumsum()


fig = px.line(df, x="date", y="like", title='Number of likes over time')

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
