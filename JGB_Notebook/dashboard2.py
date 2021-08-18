import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objects as go
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

app = dash.Dash()

app.layout = html.Div([
  html.H1('Financial Dashboard'),

  html.Div([  
  dcc.Input(id='company_selection',value='NVDA'),
  html.H3(id='text'),
  dcc.Graph(id ='revenue'),
  dcc.Graph(id ='netincome'),
  ],style= {'padding':10})
])


@app.callback(Output('revenue','figure'),
              [Input('company_selection','value')])
def retrieve_revenue(company):
    demo = os.getenv("FMP_Key")
    print(demo)
    stock = company
    print(stock)
    IS = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={demo}')
    IS = IS.json()
    print(IS)
    IS = pd.DataFrame(IS)
    Revenues = IS['revenue']
    Dates = IS['date']
    datapoints = {'data': [go.Bar(x=Dates, y=Revenues)],'layout': dict(xaxis={'title':'Date'},
                                                                      yaxis={'title':'Revenue'},
                                                                            )}
    return datapoints


@app.callback(Output('netincome','figure'),
             [Input('company_selection','value')])
def retrieve_revenue(company):
    demo = os.getenv('FMP_Key')
    print(demo)
    stock = company
    IS = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={demo}')
    IS = IS.json()
    print(IS)
    IS = pd.DataFrame(IS)
    NetIncome = IS['netIncome']
    Dates = IS['date']
    datapoints = {'data': [go.Bar(x=Dates, y=NetIncome)],'layout': dict(xaxis={'title':'Date'},
                                                                      yaxis={'title':'Net_Income'},
                                                                            )}
    return datapoints


@app.callback(
    Output(component_id='text', component_property='children'),
    [Input(component_id='company_selection', component_property='value')]
)
def update_output_div(input_value):
    return 'Displaying Data for "{}"'.format(input_value)
if __name__ == '__main__':
    app.run_server(debug=True)