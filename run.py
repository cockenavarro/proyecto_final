from dash import dcc, html
from dash.dependencies import Input, Output
from app.app import app
from layouts.precipitacion_layouts import layout
from callbacks.precipitacion_callbacks import update_output

app.layout = html.Div([
    dcc.Input(id='input-component', type='text', value=''),
    html.Div(id='output-div'),
    html.Div(id='page-content')
])

# Otros callbacks y configuraciones

if __name__ == '__main__':
    app.run_server(debug=True)
