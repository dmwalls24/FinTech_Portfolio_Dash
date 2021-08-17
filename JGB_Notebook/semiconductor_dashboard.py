## Code taken from https://gist.github.com/rpkyle/b69a4c70bb35b53c1902587a7c3e52dc

!import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html

!import requests
!import plotly.graph_objects as go

!from pandas_datareader import data as web 
from datetime import datetime as dt

app = dash.Dash()


app.layout = html.Div([
    html.H1('Semiconductor Dashboard'),

    html.Div([
    dcc.Input(id='company_selection', value=TSM),
    html.H3(id='text'),
    dcc.Graph(id='revenue'),
    dcc.Graph(id='netincome'),
    ],style={'padding':10}        
    ])    
])



@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2017, 1, 1), 
        dt.now()
    )   
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }], 
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }   

if __name__ == '__main__':
    app.run_server()