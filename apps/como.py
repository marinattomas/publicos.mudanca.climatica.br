import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from . import layout as lb
from app import app



img_home = html.Div(className='col-lg-6',
                         children=html.Img(id='img_home'))

texto_explicativo = html.Div([
                        html.H2('temos aqui um título'),
                        html.P('temos aqui um texto basjhaushaibqiebquvw')
])

especifico = html.Div([dbc.Row(justify="center"),
                        html.Br(),
                       dbc.Row(html.Div(texto_explicativo))
                       ])




texto_p="""Use essa página para entender como funciona cada uma das páginas do dashboard clicando nos links do menu abaixo"""

layout = lb.defineLayout(especifico,[True,True,True,True],texto_p,tipo_pag='outro')
