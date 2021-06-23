import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from . import layout as lb
from app import app



img_home = html.Div(className='col-lg-6',
                         children=html.Img(id='img_home'))

texto_explicativo = html.Div([
                        html.H3('Referências'),
                        dcc.Markdown('''Aqui estão algumas referências que nortearam a decisão pelo método utilizado, a interpretação dos grupos e a sugestão das campanhas. A metodologia de segmentação e o dashboard se baseou muito no estudo do programa de comunicação das mudanças climáticas de Yale, [As seis Américas das Mudanças climáticas],(https://climatecommunication.yale.edu/about/projects/global-warmings-six-americas/) e na ferramenta [Six Americas Super Short Survey](https://climatecommunication.yale.edu/visualizations-data/sassy/).

- CASTELFRANCHI, Y. et al. As opinioes dos brasileiros sobre ciencia e tecnologia: o paradoxo 
da relacao entre informacao e atitudes. **História, Ciências, Saúde-Manguinhos**, v. 20, n. suppl 1, p. 1163–1183, 30 nov. 2013.
- CENTRO DE GESTÃO E ESTUDOS ESTRATÉGICOS - CGEE. **Percepção pública da C&T no Brasil - 2019 Resumo executivo.** Brasília: Centro de Gestão e Estudos Estratégicos, 2019.
- CENTRO DE GESTÃO E ESTUDOS ESTRATÉGICOS- CGEE. **A ciência e a tecnologia no olhar dos brasileiros. Percepção pública da C&T no Brasil: 2015**. Brasília, DF: CENTRO DE GESTÃO E ESTUDOS ESTRATÉGICOS- CGEE, 2015. Disponível em:[https://www.cgee.org.br/documents/10182/734063/percepcao_web.pdf](https://www.cgee.org.br/documents/10182/734063/percepcao_web.pdf). 
- CHRYST, B. et al. Global Warming’s “Six Americas Short Survey”: Audience Segmentation of 
Climate Change Views Using a Four Question Instrument. **Environmental Communication**, v. 12, n. 8, p. 1109–1122, 17 nov. 2018.
- COLLINS, L. M.; LANZA, S. T. **Latent Class and Latent Transition Analysis**. [s.l: s.n.].
- LEISEROWITZ. **Global Warming Six americas 2009**: Yale Project on Climate Change Communication. New Haven: Yale University, 2009. Disponível em:[https://climatecommunication.yale.edu/wp-content/uploads/2016/02/2009_05_Global-Warmings-Six-Americas.pdf](https://climatecommunication.yale.edu/wp-content/uploads/2016/02/2009_05_Global-Warmings-Six-Americas.pdf)
- LEISEROWITZ, A. et al. **Global warming’s six indias**: Yale Project on Climate Change Communication. New Haven: Yale University, 2013. Disponível em: [https://climatecommunication.yale.edu/wp-content/uploads/2016/02/2013_05_Global-Warming%E2%80%99s-Six-Indias.pdf](https://climatecommunication.yale.edu/wp-content/uploads/2016/02/2013_05_Global-Warming%E2%80%99s-Six-Indias.pdf)
- LEISEROWITZ, A. et al. Global Warming’s Six Americas: a review and recommendations for climate change communication. **Current Opinion in Behavioral Sciences**, v. 42, p. 97–103, dez. 2021.
- LITTLE, T. D. (ED.). **The Oxford handbook of quantitative methods**. New York: Oxford University Press, 2013.
- MAIBACH, E. W. et al. Identifying Like-Minded Audiences for Global Warming Public Engagement Campaigns: An Audience Segmentation Analysis and Tool Development. **PLoS ONE**, v. 6, n. 3, p. e17571, 10 mar. 2011.
- MASSARANI, L. et al. **O que os jovens brasileiros pensam da ciência e da tecnologia?** 2021.
- ROSER-RENOUF, C. et al. Engaging Diverse Audiences with Climate Change: Message Strategies for Global Warming’s Six Americas. **SSRN Electronic Journal**, 2014.
                        
                        ''',className='text', style = { "padding": "10px 20px"})
                      ])

especifico = html.Div([dbc.Row(justify="center"),
                        dbc.Row(html.Div(texto_explicativo))
                       ])




texto_p="""Esta página contém informações complementares sobre os responsáveis pelo banco de dados original e as referências que basearam a escolha de campanhas para os públicos identificados e a aplicação do método de análise de classes latentes """

layout = lb.defineLayout(especifico,[True,True,True,True],texto_p,tipo_pag='outro')
