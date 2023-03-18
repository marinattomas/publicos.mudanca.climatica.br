import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.MINTY])
app.title = 'Grupos de percepção das Mudanças climáticas BR'
server = app.server
