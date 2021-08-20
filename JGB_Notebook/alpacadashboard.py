import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import alpaca_trade_api as tradeapi
import os

from dotenv import load_dotenv
load_dotenv()


alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2"
)

ticker = ["AMD", "MU", "NDVA", "TSM"]
timeframe = "1D"
start_date = pd.Timestamp("2011-08-13", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2021-08-13", tz="America/New_York").isoformat()

ticker_data = api.get_barset(
    ticker,
    timeframe,
    start=start_date,
    end=end_date,
    limit=1000,
).df
print(ticker_data)

app = dash.Dash()

app.layout = html.Div([
  html.H1('Financial Dashboard'),

  html.Div([  
  dcc.Input(id='company_selection',value='NVDA'),
  html.H3(id='text'),
  dcc.Graph(id ='ClosingPrice'),
  ],style= {'padding':10})
])

@app.callback(Output('ClosingPrice','figure'),
              [Input('company_selection','value')])
def retrieve_revenue(ticker):
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
    stock = ticker
    stock_data = ticker_data
    for 
    Closing = ticker_data[]['close']
    Dates = ticker_data['time']
    datapoints = {'data': [go.Bar(x=Dates, y=Closing)],'layout': dict(xaxis={'title':'Date'},
                                                                      yaxis={'title':'Closing'},
                                                                            )}
    return datapoints