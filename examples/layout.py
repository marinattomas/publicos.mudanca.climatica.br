import dash
import dash_core_components as dcc
import dash_html_components as html


def layout_base():
    return html.Div([
        html.Div([
        html.H1(children='FOOD FOOTPRINT'),
        html.Label('We are interested in investigating the food products that have the biggest impact on environment. Here you can understand which are the products whose productions emit more greenhouse gases and associate this with each supply chain step, their worldwide productions, and the water use.',
                    style={'color':'rgb(33 36 35)'}),
        html.Img(src=app.get_asset_url('supply_chain.png'), style={'position': 'relative', 'width': '180%', 'left': '-83px', 'top': '-20px'}),
    ], className='side_bar'),

    html.Div([
        html.Div([
            html.Div([
                html.Label("Choose the Product's Origin:"),
                html.Br(),
                html.Br(),
                radio_ani_veg
            ], className='box', style={'margin': '10px', 'padding-top':'15px', 'padding-bottom':'15px'}),

            html.Div([
                html.Div([

                    html.Div([
                        html.Label(id='title_bar'),
                        dcc.Graph(id='bar_fig'),
                        html.Div([
                            html.P(id='comment')
                        ], className='box_comment'),
                    ], className='box', style={'padding-bottom':'15px'}),

                    html.Div([
                        html.Img(src=app.get_asset_url('Food.png'), style={'width': '100%', 'position':'relative', 'opacity':'80%'}),
                    ]),

                ], style={'width': '40%'}),


                html.Div([

                    html.Div([
                    html.Label(id='choose_product', style= {'margin': '10px'}),
                    drop_map,
                    ], className='box'),

                    html.Div([
                        html.Div([
                            html.Label('Emissions measured as kg of CO2 per kg of product', style={'font-size': 'medium'}),
                            html.Br(),
                            html.Br(),
                            html.Div([
                                html.Div([
                                    html.H4('Land use', style={'font-weight':'normal'}),
                                    html.H3(id='land_use')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Animal Feed', style={'font-weight':'normal'}),
                                    html.H3(id='animal_feed')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Farm', style={'font-weight':'normal'}),
                                    html.H3(id='farm')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Processing', style={'font-weight':'normal'}),
                                    html.H3(id='processing')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Transport', style={'font-weight':'normal'}),
                                    html.H3(id='transport')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Packaging', style={'font-weight':'normal'}),
                                    html.H3(id='packging')
                                ],className='box_emissions'),

                                html.Div([
                                    html.H4('Retail', style={'font-weight':'normal'}),
                                    html.H3(id='retail')
                                ],className='box_emissions'),
                            ], style={'display': 'flex'}),

                        ], className='box', style={'heigth':'10%'}),

                        html.Div([
                            html.Div([

                                html.Div([
                                    html.Br(),
                                    html.Label(id='title_map', style={'font-size':'medium'}),
                                    html.Br(),
                                    html.Label('These quantities refer to the raw material used to produce the product selected above', style={'font-size':'9px'}),
                                ], style={'width': '70%'}),
                                html.Div([

                                ], style={'width': '5%'}),
                                html.Div([
                                    drop_continent,
                                    html.Br(),
                                    html.Br(),
                                ], style={'width': '25%'}),
                            ], className='row'),

                            dcc.Graph(id='map', style={'position':'relative', 'top':'-50px'}),

                            html.Div([
                                slider_map
                            ], style={'margin-left': '15%', 'position':'relative', 'top':'-38px'}),

                        ], className='box', style={'padding-bottom': '0px'}),
                    ]),
                ], style={'width': '60%'}),
            ], className='row'),

            html.Div([
                html.Div([
                    html.Label("3. Global greenhouse gas emissions from food production, in percentage", style={'font-size': 'medium'}),
                    html.Br(),
                    html.Label('Click on it to know more!', style={'font-size':'9px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=fig_gemissions)
                ], className='box', style={'width': '40%'}),
                html.Div([
                    html.Label("4. Freshwater withdrawals per kg of product, in Liters", style={'font-size': 'medium'}),
                    html.Br(),
                    html.Label('Click on it to know more!', style={'font-size':'9px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=fig_water)
                ], className='box', style={'width': '63%'}),
            ], className='row'),

            html.Div([
                html.Div([
                    html.P(['GroupV', html.Br(),'Ana Carrelha (20200631), Inês Melo (20200624), Inês Roque (20200644), Ricardo Nunes(20200611)'], style={'font-size':'12px'}),
                ], style={'width':'60%'}),
                html.Div([
                    html.P(['Sources ', html.Br(), html.A('Our World in Data', href='https://ourworldindata.org/', target='_blank'), ', ', html.A('Food and Agriculture Organization of the United Nations', href='http://www.fao.org/faostat/en/#data', target='_blank')], style={'font-size':'12px'})
                ], style={'width':'37%'}),
            ], className = 'footer', style={'display':'flex'}),
        ], className='main'),
    ]),
])
