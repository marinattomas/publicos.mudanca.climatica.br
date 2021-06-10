import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

texto_p = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
   standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."""

def defineLayout(especifico,ativo,texto_padrao=texto_p,tipo_pag='padrão'):

    opcoes = html.Div([dcc.Link('Conheça os dados    ', href='/apps/home'),
                        dcc.Link('Entendendo os grupos    ', href='/apps/grupos'),
                        dcc.Link('Campanhas indicadas    ', href='/apps/campanhas'),
                        dcc.Link('Seu público    ', href='/apps/publico')])

    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Mais", header=True),
                    dbc.DropdownMenuItem("Como usar", href="/apps/como"),
                    dbc.DropdownMenuItem("Sobre o projeto", href="/apps/sobre"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="PBMC - Percepção de Brasileiros das Mudanças Climáticas",
        brand_href="/apps/home",
        color="primary",
        dark=True,
        className='navbar fixed-top'
    )



    nav = dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Conhecendo os dados", active=ativo[0], href='/apps/home')),
            dbc.NavItem(dbc.NavLink("Entendendo os grupos", active=ativo[1],href='/apps/grupos')),
            dbc.NavItem(dbc.NavLink("Campanhas indicadas",active=ativo[2], href='/apps/campanhas')),
            dbc.NavItem(dbc.NavLink("Seu público", active=ativo[3], href='/apps/publico')),
        ],
        className = 'nav-tabs',
        fill = True
    )

    rodape = dbc.NavbarSimple(
        children=[html.Div('Desenvolvido e ilustrado por Marina Tomás')],
        brand_href="#",
        color="primary",
        dark=True,
        className='navbar bottom'
    )

    titulo = html.Div([html.H2('Os grupos brasileiros de percepção das mudanças climáticas',style={'padding-top':'75px','padding-bottom':'20px'}),
        html.P(f"""{texto_padrao}""",
           style={'padding-top':'10px','padding-bottom':'40px','padding-left':'25px','padding-right':'25px'})])

    if tipo_pag=='padrão':
        layout = html.Div([navbar,
                         html.Div([
                            html.Div(titulo,className='container'),
                            html.Div(nav,className='container'),
                            html.Div(especifico,className='box'),
                            ],className='container'),
                         rodape])
    else:
        layout = html.Div([navbar,
                         html.Div([
                            html.Div(titulo,className='container'),
                            html.Div(especifico,className='box'),
                            ],className='container'),
                         rodape])
    return layout
