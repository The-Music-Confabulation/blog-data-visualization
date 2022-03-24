from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import os
import plotly.io as pio

app = Dash(__name__)

server = app.server

with open('post.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

# --------------Number of posts over time------------------#
df_pot = df.groupby('date', as_index=False)['title'].count()
df_pot['title'].astype(int)
fig_1 = px.line(df_pot, x="date", y="title", title='Number of posts over time')
fig_1.update_layout(
    title_x=0.5,
    paper_bgcolor="aliceblue",
    yaxis=dict(
        tickmode='linear'
    )
)

fig_1.update_traces(mode="markers+lines")

# --------------Number of interactions over time------------------#
df['total_like'] = df.apply(lambda row: len(row['like']), axis=1)
df['total_cmt'] = df.apply(lambda row: len(row['comments']), axis=1)

df_int = df.groupby('date', as_index=False)['total_like'].sum()
df_int2 = df.groupby('date', as_index=False)['total_cmt'].sum()

fig_2 = px.line(df_int, x="date", y="total_like", title='Number of likes over time')
fig_2.update_layout(
    title_x=0.5,
    paper_bgcolor="aliceblue",
    yaxis=dict(
        tickmode='linear'
    )
)
fig_2.update_traces(mode="markers+lines")

fig_3 = px.line(df_int2, x="date", y="total_cmt", title='Number of comments over time')
fig_3.update_layout(
    title_x=0.5,
    paper_bgcolor="aliceblue",
    yaxis=dict(
        tickmode='linear'
    )
)
fig_3.update_traces(mode="markers+lines")

# --------------Rank of post by likes------------------#

fig_4 = px.bar(df, x="title", y="total_like", title='Rank of post by likes')
fig_4.update_layout(
    title_x=0.5,
    paper_bgcolor="aliceblue",
    yaxis=dict(
        tickmode='linear'
    )
)

# --------------Set Up User Schema------------------#
with open('user.json', encoding='utf-8') as inputfile:
    df_user = pd.read_json(inputfile)

# --------------Current user over time------------------#
df_user['dateJoin'] = pd.to_datetime(df_user['dateJoin'])
df_uot = df_user.groupby('dateJoin', as_index=False)['username'].count()

fig_5 = px.line(df_uot, x="dateJoin", y="username", title='Rank of post by likes')
fig_5.update_layout(
    title_x=0.5,
    paper_bgcolor="aliceblue",
    yaxis=dict(
        tickmode='linear'
    )
)
fig_5.update_traces(mode="markers+lines")
# --------------Set Up Dashboard------------------#
app.layout = html.Div(
    children=[

        html.H1(children=['Welcome to the Music Confabulation - Data Visualization'], style={'textAlign': 'center'}),

        html.Div(children=dcc.Graph(
            id='fg_1',
            figure=fig_1
        ), style={'margin': '20px', 'border': '2px solid black'}),

        # html.Div(children=dcc.Graph(
        #     id='fg_2',
        #     figure=fig_2
        # ), style={'margin': '20px', 'border': '2px solid black'}),
        #
        # html.Div(children=dcc.Graph(
        #     id='fg_3',
        #     figure=fig_3
        # ), style={'margin': '20px', 'border': '2px solid black'}),

        html.Div(children=dcc.Graph(
            id='fg_4',
            figure=fig_4
        ), style={'margin': '20px', 'border': '2px solid black'}),

        html.Div(children=dcc.Graph(
            id='fg_5',
            figure=fig_5
        ), style={'margin': '20px', 'border': '2px solid black'}),

    ], style={'margin': 'auto'})

if __name__ == '__main__':
    app.run_server(debug=True)
