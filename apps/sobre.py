import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import dash_bootstrap_components as dbc
from . import layout as lb
from app import app



img_home = html.Div(className='col-lg-6',
                         children=html.Img(id='img_home'))

texto_explicativo = html.Div([
                       html.H2('Informações Extras', style= {"padding": "10px"}),
                       html.H3('Explicações sobre a probabilidade de resposta'),
                     dcc.Markdown('''A probabilidade de resposta no gráfico da aba de grupos corresponde á
                      probabilidade de dar a resposta 1 nas perguntas escolhidas no modelo conforme a recodificação 
                      apresentada abaixo.  Baseado na teoria da análise de classes latentes interpretamos estas 
                      probabilidades nas explicações das respostas da seguinte forma:''', className='text'),
                     dcc.Markdown('''
- Probabilidades acima de 0,7 correspondem a uma probabilidade alta dos membros do grupo fornecerem uma resposta 1
- Valores entre 0,4  e 0,6 indicam um padrão de resposta dividido no grupo, ou seja existe uma probabilidade razoável que os membros do grupo tenham dado tanto a resposta 1 quanto a resposta 0.
- Probabilidades abaixo de 0,3 sugerem uma probabilidade alta dos membros do grupo optarem pela resposta 0
'''),
    html.H3('Perguntas e recodificação das variáveis'),
     dcc.Markdown('''
- O quanto você considera que está preocupado(a) com o meio ambiente atualmente? Você diria que está: "Muito preocupado(a)" corresponde á resposta 1 e demais respostas a 0.
- Você considera mais importante:"Proteger o meio ambiente, mesmo que isso signifique menos crescimento econômico e menos empregos" corresponde á resposta 1  e "Promover o crescimento econômico e a geração de empregos, mesmo que isso prejudique o meio ambiente?" á resposta 0.
- O quanto você acha importante a questão do aquecimento global? : Respostas "Muito importante"  corresponde á resposta 1 e demais respostas a 0.
- Recentemente, tem se falado bastante sobre aquecimento global, ou seja, sobre o aumento da temperatura média mundial nos últimos 150 anos, que contribui para causar mudanças no clima do planeta. Na sua opinião, o aquecimento global está acontecendo? "Sim" foi codificado como 1 e demais respostas como 0
- o aquecimento global é causado principalmente pela ação humana ou é resultado de mudanças naturais do meio ambiente? "Causado principalmente pela ação humana" corresponde á resposta 1 e demais respostas a 0.
- Opinião sobre o que os cientistas acham do aquecimento global : "A maior parte dos cientistas acha que o aquecimento global está acontecendo" foi codificado como 1  e demais respostas como 0.
- O quanto você acha que o aquecimento global pode prejudicar as próximas gerações: "Muito" e "Mais ou menos" foram codificados como 1 e demais respostas como 0
- O quanto você acha que o aquecimento global pode prejudicar você e a sua família? "Muito" e "Mais ou menos" foram codificados como 1 e demais respostas como 0

'''),
html.H3('Outras observações'),
     dcc.Markdown('''

- Apesar do questionário ter usado o termo aquecimento global por ser mais reconhecido pelo público, optamos por utilizar o termo mudanças climáticas no dashboard para descrever os grupos, ainda que esses termos não sejam sinônimos.
- As respostas "Não sei" e "Não respondeu" foram categorizadas como 0 em todas as perguntas
- A sugestão de campanhas para os públicos se baseou em estudos sobre a percepção dos brasileiros e estudos de segmentação internacionais disponíveis na página de referências''')

    ])


especifico = html.Div([dbc.Row(justify="center"),
                       #html.Br(),
                       dbc.Row(html.Div(texto_explicativo))
                       ])




texto_p="""Esta página contém informações extras que ajudam a entender como este dashboard foi produzido e como foi feita a segmentação das classes identificadas."""

layout = lb.defineLayout(especifico,[True,True,True,True],texto_p,tipo_pag='outro')
