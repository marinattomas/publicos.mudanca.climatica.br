import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home, grupos, campanhas, publico, como, sobre

server = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/home':
        return home.layout
    elif pathname == '/apps/grupos':
        return grupos.layout
    elif pathname == '/apps/campanhas':
        return campanhas.layout
    elif pathname == '/apps/publico':
        return publico.layout
    elif pathname == '/apps/como':
        return como.layout
    elif pathname == '/apps/sobre':
        return sobre.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server()
