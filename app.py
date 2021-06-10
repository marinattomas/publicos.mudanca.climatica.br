import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.MINTY])
server = app.server
app.title = 'dash maravilhoso da marina'
