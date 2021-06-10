import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
from . import layout as lb
import plotly.graph_objs as go
import dash
import plotly.graph_objects as go


nomes_classes = ['Antenados','Perdidos','Desligados','Céticos']
grupo_selecionado = 0
colors = ['#56CC9D','#FFCE67','#F96C44','#F3969A']

def plotaGraficoClasse():
    classes = pd.read_csv("Data/prop_sex.csv")
    classes =classes[classes["sex"] == 'Feminino']

    layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            title="Porcentagem",
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines,
        )
    )
    #montar a figura
    fig=go.Figure(layout=layout)
    fig.add_trace(go.Bar(
                            x = nomes_classes,
                            y = classes.freq_br,
                            marker_color=colors
    ))
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(clickmode='event+select')
    return fig


def color_perg(classe):
    if classe == 1:
        colors2 = '#56CC9D'
    elif classe == 2:
        colors2 = '#FFCE67'
    elif classe == 3:
        colors2 = '#F96C44'
    else:
        colors2 = '#F3969A'
    return colors2

def plotaGraficoPerguntas(classe):
    perguntas = pd.read_csv("Data/porcentagem_resp.csv")
    condicao_classe = "class "+ str(classe) +": "
    #filtra pra pegar uma classe só
    perguntas = perguntas[perguntas['var1']==condicao_classe]
    layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            title="probabilidade de resposta",
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines
        )
    )
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Bar(
                        x = perguntas['l1'],
                        y = perguntas['value'],
                        marker_color=color_perg(classe)
    ))
    fig.update_yaxes( range=[0,1])
    return fig

drop_class = dcc.Dropdown(
        id = 'drop_class',
        clearable=False,
        searchable=False,
        options=[{'label': 'Antenados', 'value': '1'},
                {'label': 'Perdidos', 'value': '2'},
                {'label': 'Desligados', 'value': '3'},
                {'label': 'Céticos', 'value': '4'}],
        value='1',
        style= {'margin': '4px', 'box-shadow': '0px 0px #ebb36a', 'border-color': '#ebb36a'}
    )


botoes = buttons = html.Div(
    [
        dbc.Button("Antenados", id='btn-Antenados',color="success" , className="mr-1"),
        dbc.Button("Perdidos", id='btn-Perdidos',color="warning", className="mr-1"),
        dbc.Button("Desligados", id='btn-Desligados',color="danger" , className="mr-1"),
        dbc.Button("Céticos", id='btn-Ceticos',color="secondary" , className="mr-1"),
    ]
)

grafico_classe = html.Div([dcc.Graph(id='grafico-classe',
                                    figure=plotaGraficoClasse()),
                         ],
                          className='col-lg-12')

img_explicativa = html.Div(className='col-lg-12',
                         children=html.Img(id='img-grupos'))


grafico_perguntas = html.Div([dcc.Graph(id='grafico-perguntas')],
                          className='col-lg-12')

img_pergunta = html.Div(className='col-lg-6',
                         children=html.Img(id='img-pergunta'))

especifico = html.Div( html.Div(dbc.Card(html.Div(children=[
                                                             html.Br(),
                                                            html.Div(html.H2('Entendendo seus grupos')),
                                                            #html.Br(),
                                                            html.Div(className='row',
                                                                     children=[grafico_classe
                                                                              ]),
                                                            html.Div(className='d-flex justify-content-around',
                                                                      children=[botoes]),
                                                            html.Br(),
                                                            html.Div(className='row',
                                                                     children=[
                                                                               img_explicativa]),
                                                            # html.Br(),
                                                            html.Div(className='row',
                                                                     children=[grafico_perguntas,
                                                                       img_pergunta,
                                                                       dcc.Store(id='store-grupo-selecionado')])
                                      ] ))))


layout = lb.defineLayout(especifico,[False,True,False,False])


@app.callback(
    Output('img-grupos','src'),
    Output('grafico-perguntas','figure'),
    Output('store-grupo-selecionado','data'),
    Input('grafico-classe','clickData'),
    Input('btn-Antenados','n_clicks'),
    Input('btn-Perdidos','n_clicks'),
    Input('btn-Desligados','n_clicks'),
    Input('btn-Ceticos','n_clicks')
    )
def update_img_explicativa(clickdata,btn1,btn2,btn3,btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    print('esseé ó changeid',changed_id)
    #ctx = dash.callback_context
    #ctx = ctx.triggered[0]['prop_id'].split('.')[0]
    click=0
    if 'grafico-classe' in changed_id:
        click=clickdata['points'][0]['x']

    if ('btn-Antenados' in changed_id) or (click=='Antenados'):
        grupo_selecionado = 1
        caminho = '/assets/campanha_1.png'
        fig = plotaGraficoPerguntas(1)
    elif ('btn-Perdidos' in changed_id) or (click=='Perdidos') :
        grupo_selecionado = 2
        caminho = '/assets/campanha_2.png'
        fig = plotaGraficoPerguntas(2)
    elif ('btn-Desligados' in changed_id) or (click=='Desligados'):
        grupo_selecionado = 3
        caminho = '/assets/campanha_3.png'
        fig = plotaGraficoPerguntas(3)
    elif ('btn-Ceticos' in changed_id) or (click=='Ceticos'):
        grupo_selecionado = 4
        caminho = '/assets/campanha_4.png'
        fig = plotaGraficoPerguntas(4)
    else:
        grupo_selecionado = 0
        caminho = '/assets/campanha_0.png'
        layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            title="probabilidade de resposta",
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines
            )
        )
        fig = go.Figure(layout=layout)
        fig.update_yaxes( range=[0,1])
    return caminho, fig, grupo_selecionado

@app.callback(
    Output('img-pergunta','src'),
    Input('grafico-perguntas','clickData'),
    Input('store-grupo-selecionado','data')
    )
def update_img_perguntas(clickdata,grupo_selecionado):
    ctx = dash.callback_context
    ctx = ctx.triggered[0]['prop_id'].split('.')[0]

    if ctx == 'store-grupo-selecionado':
        nome_figura = 'pergunta0.png'
    else:
        if clickdata != None:
            pergunta = clickdata['points'][0]['x']

            if pergunta == 'amb_preocupa':  id_pergunta=1
            elif pergunta == 'amb_prioridade': id_pergunta=2

            nome_figura = f"""pergunta{id_pergunta}_grupo{grupo_selecionado}.png"""
        else:
            nome_figura = 'pergunta0.png'
    print(nome_figura)
    return '/assets/'+nome_figura
