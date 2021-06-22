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




texto_p="""Esta páginas contém informações extras que ajudam a entender como este dashboard foi produzido e como foi feita a segmentação das classes identificadas."""

layout = lb.defineLayout(especifico,[True,True,True,True],texto_p,tipo_pag='outro')
