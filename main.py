from data_generator import getData
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# print(getData())


# with open('collection.json', encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile)
#
# # df.to_csv('csvfile.csv', encoding='utf-8', index=False)
#
# print(df.to_string())
# df = px.data.gapminder().query()
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()

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

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
