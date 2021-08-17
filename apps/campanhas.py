import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from . import layout as lb
import pandas as pd
import plotly.graph_objs as go
import dash
import numpy as np

nomes_classes = ['Antenados','Perdidos','Desligados','Incrédulos']
faixas_idade = ['18 a 24 anos','25 a 34 anos','35 a 44 anos','45 a 54 anos','55 anos ou mais']
colors = ['#56CC9D','#FFCE67','#F96C44','#F3969A']
cores_classe ={'1': ['#4EB98F','#56CC9D','#80D8B5','#AAE4CD','#BFEAD9','#D1F0E4' ],
               '2': ['#D19836','#DEA645','#E0AF5A','#E8BE74','#EBC686','#EBCC94'],
               '3': ['#D27A37','#DE8744','#E1955B','#E7A674','#EAB186','#EBBB94'],
               '4': ['#C24768','#CF5475','#D36986','#DC7E97','#E18EA4','#E29CAC']}
markers = ['circle','square','diamond','pentagon','hexagon','octagon']

texto_campanhas = "Nesta página você pode explorar as campanhas mais indicadas para cada um dos públicos identificados, assim como entender como esses públicos se relacionam com as variáveis sociodemográficas"

texto_grafico_socio ="Você também pode dar zoom para ver os pontos com mais detalhes, ou cliclar na legenda para filtrar quais categorias deseja mostrar"

texto_grafico_matrix ="Selecione um dos grupos e uma das variáveis para ver as características deste grupo nessa variável"
def figura_inicial():
    fig = go.Figure()
    fig.add_layout_image(x=0, y=0, xref="x", yref="y", opacity=1.0, layer="above", source="/assets/selecionar_grupos_campanha.png")
    return fig


def plotDotMatrix(df,n_linhas,total=100,asc=False):
    #montar o grafico
    fig = go.Figure()
    #gerar df de pontos (x,y) cumprindo as exigências de quantidades de linhas
    n_colunas = np.ceil(total/n_linhas) #vai sempre arredondar pra cima, pq se der decimal a 1a linha vai ser maior
    linhas = pd.DataFrame({'y':np.arange(n_linhas)})
    colunas = pd.DataFrame({'x':np.arange(n_colunas)})
    pontos = linhas.merge(colunas, how='cross')
    pontos = pontos[:total]#se sobrar ponto, tira a última linha
    pontos['cor']= '#FFFFFF'
    pontos['marker']='line-ns'
    pontos['y']=-pontos['y']
    #lidar com as porcentagens quebradinhas (aqui só rola um round-lidar com isso seriamente fora pra não >total)
    df.freq_rel = np.round(df.freq_rel.values*total/100)
    #organizar qual ponto vai ser de qual cor e marcador
    df = df.sort_values(by='label',ascending=asc).reset_index()
    df['cumsum'] = df.freq_rel.cumsum()
    print(df)
    for index, row in df.iterrows():
        if index ==0:
            pontos.loc[0:int(row['cumsum']),'cor']=row['cor']
            pontos.loc[0:int(row['cumsum']),'marker']=row['marker']
            print(row['cor'])
        else:
            pontos.loc[int(df.iloc[index-1]['cumsum']):int(row['cumsum']),'cor']=row['cor']
            pontos.loc[int(df.iloc[index-1]['cumsum']):int(row['cumsum']),'marker']=row['marker']
            print(row['cor'])
    print(pontos)
    #plota os pontinhos
    for m in df.marker.unique():
        x = pontos[pontos['marker']==m]
        fig.add_trace(go.Scatter(x=x['x'], y=x['y'], mode='markers',
                                name= df[df.cor==x.cor.unique()[0]]['label'].values[0],
                                marker_color=x.cor.unique()[0],
                                marker_symbol=x.marker.unique()[0],
                                marker_size=20, #tamanho do marcador,
                                hovertemplate ='Categoria:'))

    fig.update_layout(
        margin=dict(l=2, r=2, t=0, b=0),
        paper_bgcolor="white",
        #width=950,
        height=250,#/len(pontos.y.unique()+10),
        plot_bgcolor="white"
    )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=0.9))
    return fig

def dfBancoSocio(socio):
    dados = pd.read_csv(f"Data/prop_{socio}.csv")
    dados['marker']='circle'
    dados['cor']='black'
    #cores para cada classes
    for classe in cores_classe:
        paleta = cores_classe[classe]
        i=0
        #tons e marcadores para cada segmento socio
        for seg in dados[socio].unique():
            dados.loc[(dados[socio]==seg)&(dados['class']==int(classe)),'cor']=paleta[i]
            print([seg,classe,dados[(dados[socio]==seg)&(dados['class']==classe)]])
            dados.loc[(dados[socio]==seg),'marker']=markers[i]
            i=i+1

    return dados


def pegaFiguraDotMatrix(dados,socio,classe):
      dados = dfBancoSocio(socio)
      dados = dados[dados['class']==classe]
      dados = dados.rename(columns= {socio:'label','freq_class':'freq_rel'})
      dados = dados.sort_values('label')
      dados = dados.astype({'freq_rel':'float'})
      fig = plotDotMatrix(dados,5,total=100,asc=True)
      return fig

def plotDumbbell(dados,socio):
     #dados = dfBancoSocio(socio)
     print('aqui',dados)
     #montar a fugura
     layout = go.Layout(
         plot_bgcolor="#FFF",  # Sets background color to white
         xaxis=dict(
             linecolor="#BCCCDC",  # Sets color of X-axis line
             showgrid=False  # Removes X-axis grid lines
         ),
         yaxis=dict(
             linecolor="#BCCCDC",  # Sets color of Y-axis line
             showgrid=False,  # Removes Y-axis grid lines
         )
     )
     fig = go.Figure(layout=layout)
     # efetivamente plotar as coisas
     for seg in dados[socio].unique():
         filtrados = dados[dados[socio]==seg]
         fig.add_trace(go.Scatter(
                                 y= nomes_classes,
                                 x= np.round(filtrados.freq_socio,2),
                                 marker=dict(color=colors, size=15,symbol=filtrados.marker.unique()[0],opacity=0.7),
                                 mode="markers",
                                 name=filtrados[socio].unique()[0]
                                 ))

     fig.add_trace(go.Scatter(
                            y = nomes_classes,
                            x = np.round(dados.freq_br,2),
                            marker=dict(color="grey", size=15,opacity=0.5),
                            mode="markers",
                            name="Nacional"
                            ))
     #mudar os ticks nos eixos
     fig.update_xaxes(title_text='Frequência Relativa (%)')
     fig.update_layout(hovermode="x unified")
     fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
        ))
     return fig








def caminho_graf_social(socio):
    if socio == 'genero':
        classes = pd.read_csv("Data/prop_sex.csv")
    elif socio == 'religiao':
        classes = pd.read_csv("Data/prop_RELIGIAO.csv")
    elif socio == 'regiao':
        classes = pd.read_csv("Data/prop_REGIAO.csv")
    elif socio == 'raca':
        classes = pd.read_csv("Data/prop_RACA.csv")
    elif socio == 'Posicao_politica':
        classes = pd.read_csv("Data/prop_Posicao_politica.csv")
    elif socio == 'classe':
        classes = pd.read_csv("Data/prop_CLASSE.csv")
    elif socio == 'raca':
        classes = pd.read_csv("Data/prop_ESCOLARIDADE.csv")
    elif socio == 'posicao_idade':
        classes = pd.read_csv("Data/prop_idade_c.csv")
    elif socio == 'posicao_internet':
        classes = pd.read_csv("Data/prop_internet_uso.csv")
    return classes

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

#CLASSE é um número de 1 a 4 representando a classes
#socio é um valor do dropdown que indica o banco
def plotaGrafico_socio(socio,classe):
    dados = pd.read_csv(f"Data/prop_{socio}.csv")

    #filtrar numa classe específica
    filtrados = dados[dados['class']==classe]
    #quais são as séries
    series = dados[socio].unique()


    #montar a fugura
    layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines
        )
    )
    fig = go.Figure(layout=layout)

    i=0
    for serie in series:
        i = i+1
        fig.add_trace(go.Bar(
                        y= [i],
                        x = filtrados[filtrados[socio] == serie].freq_class,
                        orientation='h',
                        marker_color= color_perg(classe)
                        ))


    return fig


def plotaGrafico_comp(socio):
    classes = caminho_graf_social(socio)
    classes_fem =classes[classes["sex"] == 'Feminino']
    classes_masc =classes[classes["sex"] == 'Masculino']
    layout = go.Layout(
        plot_bgcolor="#FFF",  # Sets background color to white
        xaxis=dict(
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False  # Removes X-axis grid lines
        ),
        yaxis=dict(
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines
        )
    )
    fig = go.Figure(layout=layout)
    #montar a figura
    fig.add_trace(go.Scatter(

                            y= classes["class"],
                            x= classes_fem.freq_socio,
                            marker=dict(color="crimson", size=12),
                            mode="markers",
                            name="Mulheres"
                            ))
    fig.add_trace(go.Scatter(
                            y= classes["class"],
                            x= classes_masc.freq_socio,
                            marker=dict(color="blue", size=12),
                            mode="markers",
                            name="Homens"
                            ))
    fig.add_trace(go.Scatter(
                            y = classes["class"],
                            x = classes.freq_br,
                            marker=dict(color="grey", size=12),
                            mode="markers",
                            name="Nacional"
                            ))
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.01
    ))
    return fig





#grafico clase tem as 4 classes pra selecionar
grafico_comp = html.Div([dcc.Graph(id='grafico-classe',
                                    figure=plotaGrafico_comp("genero")),
                          ])

#grafico socio tem um sociodemográficos selecionado em UMA CLASSE SÓ
grafico_socio = html.Div([dcc.Graph(id='grafico-socio',
                                    figure=plotaGrafico_socio("sex",1),
                                                    )
                          ])

botoes = buttons = html.Div(
    [
        dbc.Button("Antenados", id='btn-Antenados',color="success" , className="mr-1"),
        dbc.Button("Perdidos", id='btn-Perdidos',color="warning", className="mr-1"),
        dbc.Button("Desligados", id='btn-Desligados',color="danger" , className="mr-1"),
        dbc.Button("Incrédulos", id='btn-Ceticos',color="secondary" , className="mr-1"),
    ]
)


drop_socio = dcc.Dropdown(
        id = 'drop_socio',
        clearable=False,
        searchable=False,
        options=[{'label': 'Genero', 'value': 'sex'},
                {'label': 'Faixa de idade', 'value': 'idade_c'},
                {'label': 'Escolaridade', 'value': 'ESCOLARIDADE'},
                {'label': 'Região', 'value': 'REGIAO'},
                {'label': 'Religião', 'value': 'RELIGIAO'},
                {'label': 'Classe social', 'value': 'CLASSE'},
                {'label': 'Posição política', 'value': 'Posicao_politica'},
                {'label': 'Raça', 'value': 'RACA'},
                {'label': 'Uso de internet', 'value': 'internet_uso'},
                 ],
        value='sex', ###duvida se pode deixar geral
        style= {'margin': '4px', 'box-shadow': '0px 0px #ebb36a', 'border-color': '#ebb36a'}
    )


img_campanhas = html.Div(className='col-lg-12',
                         children=html.Img(id='img_campanhas',className="img-fluid"))

especifico = html.Div(
                [html.Div(className="row",
                          children=[
                             dbc.Col(dbc.Card(html.Div(className="col-12",
                                                children=[
                                                    html.Br(),
                                                    html.Div(html.H2('Veja as campanhas indicadas para cada público:')),
                                                    dcc.Markdown(texto_campanhas, className='text'),
                                                    #html.Br(),
                                                    img_campanhas,
                                                    html.Br(),
                                                    html.Div(className='d-flex justify-content-around',
                                                                      children=[botoes]),
                                                    dcc.Markdown("Para mais informações sobre as referências usadas para criar as campanhas acesse a página [Referências](/apps/referencias)", className='text'),

                                                        ]
                                                )
                                              ),className='col-lg-12'
                                       ),
                            dbc.Col(dbc.Card(html.Div( children=[
                                                    html.Br(),
                                                    html.H2('Veja as características deste público'),
                                                    dcc.Markdown(texto_grafico_matrix, style={"margin":30}),
                                                    html.Div(drop_socio,style={"margin":20} ),
                                                    html.Div(className='col-lg-12',
                                                             children=grafico_socio),
                                                    html.Div([dcc.Store(id='store-grupo-selecionado-campanhas')]),
                                   html.Br(),
                                   html.H2('Veja como os públicos se relacionam com as variáveis sociodemográficas:'),
                                   dcc.Markdown(texto_grafico_socio, style={"margin":30} ),
                                   grafico_comp
                                   #html.Div(grafico_classe)
                                                        ]
                                                )
                                       ),className='col-lg-12'
                                      )
                                ]
                          )
                 ])


layout = lb.defineLayout(especifico,[False,False,True,False])


@app.callback(
    Output('img_campanhas','src'),
    Output('store-grupo-selecionado-campanhas','data'),
    Input('btn-Antenados','n_clicks'),
    Input('btn-Perdidos','n_clicks'),
    Input('btn-Desligados','n_clicks'),
    Input('btn-Ceticos','n_clicks')
    )
def update_img_campanhas(btn1,btn2,btn3,btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-Antenados' in changed_id:
        grupo=1
        caminho = '/assets/campanha_1.png'
        fig = go.Figure()
    elif 'btn-Perdidos' in changed_id:
        grupo=2
        caminho = '/assets/campanha_2.png'
        fig = go.Figure()
    elif 'btn-Desligados' in changed_id:
        grupo=3
        caminho = '/assets/campanha_3.png'
        fig = go.Figure()
    elif 'btn-Ceticos' in changed_id:
        grupo=4
        caminho = '/assets/campanha_4.png'
        fig = go.Figure()
    else:
        grupo=0
        caminho = '/assets/campanha_0.png'
        layout = go.Layout(
            plot_bgcolor="#FFF",  # Sets background color to white
            xaxis=dict(
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
    return caminho,grupo

@app.callback(
    Output('grafico-socio','figure'),
    Output('grafico-classe','figure'),
    Input('drop_socio','value'),
    Input('store-grupo-selecionado-campanhas','data')
)
def update_img_socio(socio_selecionado,grupo):
    dados = dfBancoSocio(socio_selecionado)
    fig1 = pegaFiguraDotMatrix(dados,socio_selecionado,grupo)
    fig2 = plotDumbbell(dados,socio_selecionado)
    return fig1, fig2
