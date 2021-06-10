import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from . import layout as lb
import pandas as pd
import plotly.graph_objs as go
import dash


nomes_classes = ['Antenados','Perdidos','Desligados','Céticos']
colors = ['#56CC9D','#FFCE67','#F96C44','#F3969A']
dict_nomes = {'sex':'Data/prop_sex.csv',
              'idade_c':'Data/prop_idade_c.csv',
              'ESCOLARIDADE':'Data/prop_ESCOLARIDADE.csv',
              'CLASSE':'Data/prop_CLASSE.csv',
              'Posicao_politica':'Data/prop_Posicao_politica.csv',
              'RACA':'Data/prop_RACA.csv',
              'REGIAO':'Data/prop_REGIAO.csv',
              'RELIGIAO':'Data/prop_RELIGIAO.csv',
              'internet_uso':'Data/prop_internet_uso.csv',
              }


## define função para gerar os gráficos
def plotaGraficoClasse(socio,filtros):
    print(socio,filtros)
    dados = pd.read_csv(dict_nomes[socio])

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
                            y = dados.freq_br,
                            marker_color="#C8C8C8"
    ))

    #aplicar os filtros
    #se não tiver nenhum filtro ativado, só vai mostrar o do brasileiros
    if len(filtros)>0:
        #se tiver filtro, vai ter filtro ue: monta aqui a condição do filtro numa string
        filtrados=pd.DataFrame()
        for filtro in filtros:
            df = dados[dados[socio]==filtro]
            filtrados = filtrados.append(df, ignore_index=True)

        print(filtrados)

        #faz a conta pra determinar  o que vai ser plotado
        df_plot = pd.DataFrame(columns=['class','freq_plot'])
        for classe in filtrados['class'].unique():
            valor = filtrados[filtrados['class']==classe].Freq.sum()/filtrados.Freq.sum()*100
            df_plot = df_plot.append({'class':classe,'freq_plot':valor}, ignore_index=True)

        fig.add_trace(go.Bar(
                            x = nomes_classes,
                            y =df_plot.freq_plot,
                            marker_color=colors
                            ))
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(margin=dict(l=15, r=15, t=5, b=25),showlegend=False)


    return fig


## sessão de checklists dos sociodemográficos
checklist_genero = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Mulheres', 'value': 'Feminino'},
                    {'label': 'Homens', 'value': 'Masculino'},
            ],
            value=[ ],
            id="switches-genero",
            inline=True,
            switch=True
        ),
    ]
)

checklist_idade = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': '18 a 24', 'value': '18 a 24'},
                    {'label': '25 a 34', 'value': '25 a 34'},
                    {'label': '35 a 44', 'value': '35 a 44'},
                    {'label': '45 a 54', 'value': '45 a 54'},
                    {'label': '55 e +', 'value': '55 e +'},
            ],
            value=[ ],
            id="switches-idade",
            inline=True,
            switch=True
        ),
    ]
)

checklist_escolaridade = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Até primário', 'value': 'Até primário'},
                    {'label': 'Ginásio', 'value': 'Ginásio'},
                    {'label': 'Colegial', 'value': 'Colegial'},
                    {'label': 'Superior', 'value':'Superior'},
            ],
            value=[],
            id="switches-escolaridade",
            inline=True,
            switch=True
        ),
    ]
)

checklist_regiao = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Norte', 'value': 'Norte'},
                    {'label': 'Nordeste', 'value':'Nordeste'},
                    {'label': 'Centro Oeste', 'value': 'Centro Oeste'},
                    {'label': 'Sudeste', 'value':'Sudeste'},
                    {'label': 'Sul', 'value':'Sul'},
            ],
            value=[ ],
            id="switches-regiao",
            inline=True,
            switch=True
        ),
    ]
)

checklist_classe = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'A', 'value':  'A'},
                    {'label': 'B1', 'value': 'B1'},
                    {'label': 'B2', 'value':'B2'},
                    {'label': 'C1', 'value': 'C1'},
                    {'label': 'C2', 'value': 'C2'},
                    {'label': 'DE', 'value': 'DE'},
            ],
            value=[ ],
            id="switches-classe",
            inline=True,
            switch=True
        ),
    ]
)


checklist_religiao = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Católica', 'value': 'Católica'},
                    {'label': 'Protestante', 'value': 'Protestante'},
                    {'label': 'Outras Religiões', 'value': 'Outras Religiões'},
                    {'label': 'Ateu/Agnóstico/Não segue religião', 'value': 'Ateu'},
            ],
            value=[],
            id="switches-religiao",
            inline=True,
            switch=True
        ),
    ]
)

checklist_posicao = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Mais à esquerda', 'value':'Mais á esquerda'},
                    {'label': 'No centro ', 'value': 'No centro ou'},
                    {'label': 'Mais à direita', 'value': 'Mais á direita'},
            ],
            value=[ ],
            id="switches-posicao",
            inline=True,
            switch=True
        ),
    ]
)

checklist_raca = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Branca', 'value': 'Branca'},
                    {'label': 'Preta', 'value':  'Preta'},
                    {'label': 'Parda', 'value': 'Parda'},
                    {'label': 'Amarela', 'value': 'Amarela'},
                    {'label': 'Indígena', 'value': 'Indígena'},
            ],
            value=[ ],
            id="switches-raca",
            inline=True,
            switch=True
        ),
    ]
)

checklist_internet = dbc.FormGroup(
    [
        dbc.Label("Escolha um:"),
        dbc.Checklist(
            options=[
                    {'label': 'Não acessam a Internet', 'value': 'sem_internet'},
                    {'label': 'Acessa por Wi-fi', 'value': 'internet_wifi'},
                    {'label': 'Acesso apenas por Rede do celular,', 'value': 'internet_3g'},
            ],
            value=[ ],
            id="switches-internet",
            inline=True,
            switch=True
        ),
    ]
)

## organiza os checklists no layout

def sliderselect(socio):
    if socio == "Gênero":
        check = checklist_genero
    elif socio == "Idade":
        check = checklist_idade
    elif socio == "Escolaridade":
         check = checklist_escolaridade
    elif socio == "Região":
        check = checklist_regiao
    elif socio == "Classe social":
         check = checklist_classe
    elif socio == "Religião":
         check = checklist_religiao
    elif socio == "Posição política":
        check = checklist_posicao
    elif socio == "Raça":
         check = checklist_raca
    elif socio == "Acesso à internet":
         check = checklist_internet
    return check

## inclui checklists e gráficos no layout

def card_mapa(socio):
    card =  dbc.Card(html.Div(
                    children=[html.H2(socio),
                                html.Br(),
                                sliderselect(socio),
                                html.Div([dcc.Graph(id=f"grafico-classe-{socio}",figure=plotaGraficoClasse('sex',[])),])
                                ]
                     )
           )
    return card


rows_cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_mapa("Gênero"), className='col-lg-4'),
                dbc.Col(card_mapa("Idade"), className='col-lg-4'),
                dbc.Col(card_mapa("Escolaridade"), className='col-lg-4'),
                dbc.Col(html.Div(  card_mapa("Região")),  className='col-lg-4'),
                dbc.Col(html.Div(card_mapa("Classe social")),  className='col-lg-4'),
                dbc.Col(html.Div(card_mapa("Religião")),  className='col-lg-4'),
                dbc.Col(html.Div(card_mapa("Posição política")),  className='col-lg-4'),
                dbc.Col(html.Div(card_mapa("Raça")),  className='col-lg-4'),
                dbc.Col(html.Div(card_mapa("Acesso à internet")), className='col-lg-4')
            ],
            align="start",
        ),

    ]
)


especifico = html.Div([html.H2('Publico'),
                       html.Br(),
                       html.H3('Defina seu público aqui'),
                      rows_cards
                        ])



layout = lb.defineLayout(especifico,[False,False,False,True])

# Callbacks

######GENERO
@app.callback(
    Output('grafico-classe-Gênero','figure'),
    Input('switches-genero','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('sex',sw_values)
    return fig

####IDADE####
@app.callback(
    Output('grafico-classe-Idade','figure'),
    Input('switches-idade','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('idade_c',sw_values)
    return fig

####Escolaridade
@app.callback(
    Output('grafico-classe-Escolaridade','figure'),
    Input('switches-escolaridade','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('ESCOLARIDADE',sw_values)
    return fig

### REGIAO ###
@app.callback(
    Output('grafico-classe-Região','figure'),
    Input('switches-regiao','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('REGIAO',sw_values)
    return fig

###CLASSE SOCIAL
@app.callback(
    Output('grafico-classe-Classe social','figure'),
    Input('switches-classe','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('CLASSE',sw_values)
    return fig

### RELIGIAO ###
@app.callback(
    Output('grafico-classe-Religião','figure'),
    Input('switches-religiao','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('RELIGIAO',sw_values)
    return fig

#### POSICAO POLITICA
@app.callback(
    Output('grafico-classe-Posição política','figure'),
    Input('switches-posicao','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('Posicao_politica',sw_values)
    return fig

###RACA
@app.callback(
    Output('grafico-classe-Raça','figure'),
    Input('switches-raca','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('RACA',sw_values)
    return fig

### INTERNET
@app.callback(
    Output('grafico-classe-Acesso à internet','figure'),
    Input('switches-internet','value')
)
def update_fig_genero(sw_values):
    fig = plotaGraficoClasse('internet_uso',sw_values)
    return fig
