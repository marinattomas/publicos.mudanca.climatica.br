import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

texto_p = """
Esse dashboard utiliza os dados da pesquisa MUDANÇAS CLIMÁTICAS NA PERCEPÇÃO DOS BRASILEIROS para identificar quais são os grupos de percepção sobre as mudanças climáticas presentes no Brasil através análise de classes latentes.
      
A pesquisa original é uma parceria do  ITS, com o programa de comunicação das mudanças climáticas da Universidade de Yale (Yale Program on Climate Change Communication), e o dashboard é um produto do programa de bolsas desta mesma pesquisa. As entrevistas foram realizadas  entre os dias 24 de setembro a 16 de outubro de 2020 pelo IBOPE Inteligência e mais informações estão disponíveis no endereço [https://www.percepcaoclimatica.com.br/](https://www.percepcaoclimatica.com.br/)"""

def defineLayout(especifico,ativo,texto_padrao=texto_p,tipo_pag='padrão'):

    opcoes = html.Div([dcc.Link('Conheça os dados    ', href='/apps/home'),
                        dcc.Link('Entendendo os grupos    ', href='/apps/grupos'),
                        dcc.Link('Campanhas indicadas    ', href='/apps/campanhas'),
                        dcc.Link('Seu público    ', href='/apps/publico')])

    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Mais Informações", header=True),
                    dbc.DropdownMenuItem("Referências", href="/apps/referencias"),
                    dbc.DropdownMenuItem("Informações gerais", href="/apps/sobre"),
                ],
                nav=True,
                in_navbar=True,
                label="Mais informações",
            ),
        ],
        brand="Percepção dos Brasileiros sobre as Mudanças Climáticas",
        brand_href="/apps/home",
        color="primary",
        dark=True,
        className='navbar fixed-top',
        style={'padding-left':'25px'}
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
        children=[html.Div(dcc.Markdown('Desenvolvido e ilustrado por [Marina Tomás](https://linktr.ee/sciartmari)'))],
        brand_href="#",
        color="primary",
        dark=True,
        className='navbar bottom'
    )

    titulo = html.Div([html.H2('Os grupos brasileiros de percepção das mudanças climáticas',style={'padding-top':'75px','padding-bottom':'20px','padding-left':'25px','padding-right':'25px'}),
         dcc.Markdown(f"""{texto_padrao}""",
           style={'padding-top':'10px','padding-bottom':'40px','padding-left':'25px','padding-right':'25px','text-align': 'justify'})])

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
