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




texto_p="""Esta página contém informações complementares sobre os responsáveis pelo banco de dados original e as referências que basearam a escolha de campanhas para os públicos identificados e a aplicação do método de análise de classes latentes """

layout = lb.defineLayout(especifico,[True,True,True,True],texto_p,tipo_pag='outro')
