import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import dash_bootstrap_components as dbc
from src import app
from . import layout as lb
import pandas as pd
import plotly.graph_objs as go
import dash

button_group = dbc.ButtonGroup(
    [dbc.Button("pag 1",color="info", id='btn-pag_1'),
     dbc.Button("pag 2",color="info",id='btn-pag_2'),
     dbc.Button("pag 3",color="info",id='btn-pag_3'),
     dbc.Button("pag 4",color="info",id='btn-pag_4')]
)



img_home = html.Div(className='col-lg-12',
                         children=html.Img(id='img_home',className="img-fluid"))

especifico = html.Div([dbc.Row(button_group, justify="center"),
                        html.Br(),
                       dbc.Row(img_home)
                       ])


layout = lb.defineLayout(especifico,[True,False,False,False])

@app.callback(
    Output('img_home','src'),
    Input('btn-pag_1','n_clicks'),
    Input('btn-pag_2','n_clicks'),
    Input('btn-pag_3','n_clicks'),
    Input('btn-pag_4','n_clicks')
    )
def update_img_home(btn1,btn2,btn3,btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-pag_1' in changed_id:
        caminho = '/assets/home_1.png'
        fig = go.Figure()
    elif 'btn-pag_2' in changed_id:
        caminho = '/assets/home_2.png'
        fig = go.Figure()
    elif 'btn-pag_3' in changed_id:
        caminho = '/assets/home_3.png'
        fig = go.Figure()
    elif 'btn-pag_4' in changed_id:
        caminho = '/assets/home_4.png'
        fig = go.Figure()
    else:
        caminho = '/assets/home_1.png'
        fig = go.Figure()
    return caminho
