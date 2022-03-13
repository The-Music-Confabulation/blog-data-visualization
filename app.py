
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

app = Dash(__name__)

server = app.server

with open('collection.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df['total_like'] = df['like'].cumsum()

# df['test'] =


fig = px.line(df, x="date", y="like", title='Number of likes over time')

fig.update_layout(
    paper_bgcolor="LightSteelBlue",
    title_x=0.5
)

fig.update_traces(mode="markers+lines")

df2 = df.groupby('date', as_index=False)['_id'].count()

fig_2 = px.line(df2, x="date", y="_id", title='Number of posts over time')
fig_2.update_layout(
    paper_bgcolor="LightSteelBlue",
    title_x=0.5
)

fig_2.update_traces(mode="markers+lines")

fig_3 = px.bar(df, x="title", y="like", title='Posts and likes')
fig_3.update_layout(
    paper_bgcolor="LightSteelBlue",
    title_x=0.5
)


app.layout = html.Div(
    children=[

        html.H1(children=['Welcome to the Music Confabulation - Data Visualization'], style={'textAlign': 'center'}),

        html.Div(children=dcc.Graph(
            id='example-graph',
            figure=fig
        ), style={'margin': '20px'})
        ,
        html.Div(children=dcc.Graph(
                id='example-graph-2',
                figure=fig_2
        ), style={'margin': '20px'}),

        html.Div(children=dcc.Graph(
                id='example-graph-3',
                figure=fig_3
        ), style={'margin': '20px'})

    ], style={'margin': 'auto', 'border': '2px solid black'})

if __name__ == '__main__':
    app.run_server(debug=True)
