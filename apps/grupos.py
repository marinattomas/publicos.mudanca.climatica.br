from dash.dependencies import Input, Output
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
from . import layout as lb
import plotly.graph_objs as go
import dash
import plotly.graph_objects as go


nomes_classes = ['Antenados','Perdidos','Desligados','Incrédulos']
grupo_selecionado = 0
colors = ['#56CC9D','#FFCE67','#F96C44','#F3969A']
dict_perguntas  = ["Probabilidade de responder <br> que está muito preocupado</br> com o meio ambiente",
"Probabilidade de responder <br>que a pioriza proteger</br>o meio ambiente",
"Probabilidade de responder <br> que o aquecimento global </br> é importante",
"Probabilidade de responder <br> que as mudanças climáticas</br> estão acontecendo",
"Probabilidade de responder <br> que as mudanças climáticas</br> são causadas por humanos",
"Probabilidade de responder <br> que os cientistas acreditam que as </br> mudanças climáticas estão acontecendo",
"Probabilidade de responder <br>que as mudanças climáticas podem </br> prejudicar as gerações futuras",
"Probabilidade de responder <br> que as mudanças climáticas podem</br> prejudicar você e a sua família"
]

perguntas_resumo = [ 'Preocupação ambiental', 'Priorização ambiental','Importancia Climática','Crença climática','Crença causas humanas','Crença consenso','Preocupação com futuro','Preocupação pessoal']
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
                            marker_color= colors,
                            hovertemplate ='<i>%{x}</i>: '
                                           +'<br>%{y:.2f}%<extra></extra></br>',
                            hoverlabel=dict(
                            font_size=14)
    ))
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(clickmode='event+select')
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
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
                        marker_color=color_perg(classe),
                        hovertemplate ='<b>%{text}</b>:%{y:.2f}<extra></extra>',
                        text = dict_perguntas
    ))
    fig.update_yaxes( range=[0,1])
    fig.update_layout(
        xaxis = dict(
        tickmode = 'array',tickvals = perguntas['l1'],ticktext= perguntas_resumo))
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    return fig

drop_class = dcc.Dropdown(
        id = 'drop_class',
        clearable=False,
        searchable=False,
        options=[{'label': 'Antenados', 'value': '1'},
                {'label': 'Perdidos', 'value': '2'},
                {'label': 'Desligados', 'value': '3'},
                {'label': 'Incrédulos', 'value': '4'}],
        value='1',
        style= {'margin': '4px', 'box-shadow': '0px 0px #ebb36a', 'border-color': '#ebb36a'}
    )


botoes = buttons = html.Div(
    [
        dbc.Button("Antenados", id='btn-Antenados',color="success" , className="mr-1"),
        dbc.Button("Perdidos", id='btn-Perdidos',color="warning", className="mr-1"),
        dbc.Button("Desligados", id='btn-Desligados',color="danger" , className="mr-1"),
        dbc.Button("Incrédulos", id='btn-Ceticos',color="secondary" , className="mr-1"),
    ]
)

grafico_classe = html.Div([dcc.Graph(id='grafico-classe',
                                    figure=plotaGraficoClasse()),
                         ],
                          className='col-lg-12')

img_explicativa = html.Div(className='col-lg-12',
                         children=html.Img(id='img-grupos',className="img-fluid"))

def figura_inicial():
    fig = go.Figure()
    fig.add_layout_image(x=0, y=0, xref="x", yref="y", opacity=1.0, layer="above", source="/assets/selecionar_grupos.png")
    return fig


grafico_perguntas = html.Div([dcc.Graph(id='grafico-perguntas', figure = figura_inicial())],
                          className='col-lg-12')

img_pergunta = html.Div(className='col-lg-12',
                         children=html.Img(id='img-pergunta',className="img-fluid"))

especifico = html.Div( html.Div(dbc.Card(html.Div(children=[
                                                            html.Br(),
                                                            html.Div(html.H2('Entendendo seus grupos')),
                                                            dcc.Markdown("O gráfico abaixo mostra as porcentagens de cada uma das audiências identificadas na população brasileira, clique nas barras ou nos botões abaixo para entender mais sobre cada uma delas.", className='text'),
                                                            #html.Br(),
                                                            html.Div(className='row',
                                                                     children=[grafico_classe
                                                                              ]),
                                                            #html.Br(),
                                                            html.Div(className='row',
                                                                     children=[
                                                                               img_explicativa]),
                                                            html.Div(className='text',
                                                                     id='text_grupos'),
                                                            #html.Br(),
                                                            html.Div(className='d-flex justify-content-around',
                                                                      children=[botoes]),
                                                            html.Div(className='row',
                                                                     children=[grafico_perguntas,
                                                                       img_pergunta,
                                                                       dcc.Store(id='store-grupo-selecionado')]),
                                                            dcc.Markdown("Para mais informações sobre as perguntas e opções de respostas acesse a página [Informações gerais](/apps/sobre)", className='text'),

                                      ] ))))


layout = lb.defineLayout(especifico,[False,True,False,False])


@app.callback(
    Output('img-grupos','src'),
    Output('grafico-perguntas','figure'),
    Output('store-grupo-selecionado','data'),
    Output('text_grupos','children'),
    Input('grafico-classe','clickData'),
    Input('btn-Antenados','n_clicks'),
    Input('btn-Perdidos','n_clicks'),
    Input('btn-Desligados','n_clicks'),
    Input('btn-Ceticos','n_clicks')
    )
def update_img_explicativa(clickdata,btn1,btn2,btn3,btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    click=0
    if 'grafico-classe' in changed_id:
        click=clickdata['points'][0]['x']
    if ('btn-Antenados' in changed_id) or (click=='Antenados'):
        grupo_selecionado = 1
        caminho = '/assets/publico_1.png'
        fig = plotaGraficoPerguntas(1)
        text = "Os antenados são aqueles que acreditam que as mudanças climáticas são reais e se tratam de um tema importante." \
               " Eles se preocupam com o meio ambiente e  priorizam sua proteção mesmo que isso signifique um menor crescimento econômico " \
               "e menos empregos. Este grupo tem conhecimento de que as mudanças climáticas têm causa humana e que os cientistas concordam " \
               "que elas estão acontecendo, e acreditam que as mudanças climáticas vão afetar as gerações futuras e também a eles mesmos ou" \
               " sua família."
    elif ('btn-Perdidos' in changed_id) or (click=='Perdidos') :
        grupo_selecionado = 2
        caminho = '/assets/publico_2.png'
        fig = plotaGraficoPerguntas(2)
        text = "Os Perdidos, assim como os Antenados, acreditam que as mudanças climáticas são reais e importantes, " \
               "ainda que com uma probabilidade um pouco menor. O grupo também concorda que as mudanças climáticas afetarão " \
               "eles mesmos ou sua família, e também as gerações futuras.  Nas demais perguntas, porém, este grupo não tem " \
               "tanta certeza. A maioria ainda acredita que as mudanças climáticas têm causa humana, mas nem todos os membros " \
               "afirmam estar preocupados com o meio ambiente, que acham mais importante proteger o meio ambiente mesmo que " \
               "isso signifique um menor crescimento econômico e que os cientistas concordam que as mudanças climáticas estão acontecendo."
    elif ('btn-Desligados' in changed_id) or (click=='Desligados'):
        grupo_selecionado = 3
        caminho = '/assets/publico_3.png'
        fig = plotaGraficoPerguntas(3)
        text= "Os desligados acreditam que as mudanças climáticas são reais e importantes, e tem uma alta probabilidade de " \
               "responder que a causa delas é a ação humana e que os cientistas concordam que elas estão acontecendo, ainda que" \
               " com uma probabilidade menor que os Antenados. Este grupo, porém está dividido sobre proteger o meio ambiente ou" \
               " promover o crescimento econômico, tem baixa probabilidade de responder que se preocupa com o meio ambiente e nenhum" \
               " dos membros acredita que as mudanças climáticas irão impactar sua família ou eles pessoalmente. Já se tratando do futuro" \
               " os membros estão divididos, com uma ligeira maioria acreditando que as mudanças climáticas vão afetar as próximas gerações."
    elif ('btn-Ceticos' in changed_id) or (click=='Incrédulos'):
        grupo_selecionado = 4
        caminho = '/assets/publico_4.png'
        fig = plotaGraficoPerguntas(4)
        text='Os Incrédulos não acreditam que as mudanças climáticas são reais, tem causa humana, que os cientistas ' \
               'concordam ou que estas vão afetar sua família, eles mesmos ou as próximas gerações. Este grupo considera ' \
               'mais importante promover o crescimento econômico e a geração de empregos, mesmo que isso prejudique o meio' \
               ' ambiente, e tem baixa probabilidade de se declarar preocupado com o meio ambiente. Apenas na pergunta se o ' \
               'aquecimento global é uma questão importante alguns membros apresentaram respostas divergentes, ainda que  a maioria declarou que não.'
    else:
        grupo_selecionado = 0
        caminho = '/assets/publico_0.png'
        layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            title="probabilidade de resposta",
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines,
            )
        )
        fig = go.Figure(layout=layout)
        fig.update_yaxes( range=[0,1])
        #fig = figura_inicial()
        text = ""

    return caminho, fig, grupo_selecionado,text

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
            elif pergunta == 'clima_importante': id_pergunta=3
            elif pergunta == 'clima_acontecendo': id_pergunta=4
            elif pergunta == 'clima_humano_j': id_pergunta=5
            elif pergunta == 'clima_cientista_conc': id_pergunta=6
            elif pergunta == 'clima_futuro': id_pergunta=7
            elif pergunta == 'clima_voce': id_pergunta=8

            nome_figura = f"""pergunta{id_pergunta}_grupo{grupo_selecionado}.png"""
        else:
            nome_figura = 'pergunta0.png'
    print(nome_figura)
    return '/assets/'+nome_figura

