from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import json
import plotly
import plotly.express as px
import requests

app = Flask(__name__)

@app.route("/")
def index_handler():

    response = requests.get('http://127.0.0.1:5000/data')
    aList = []
    bList = []

    for el in response.json():
        aList.append(el['a'])
        bList.append(el['b'])

    df = pd.DataFrame({
      'a': aList,
      'b': bList
    })
    fig = px.line(df, x='a', y='b', title='Pls hire me!', category_orders={"a": [*range(0, 100, 1)], "b": [*range(0, 9, 1)]},)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)
    
@app.route("/data")
def data_handler():
    return get_df().to_json(orient='records')
    
def get_df():
    data = np.array([['a','b']])
    
    for x in range(1000):
        a = np.random.randint(101, size=1)[0]
        b = a % 10
        data = np.append(data, [[a, b]], axis=0)
 
    return pd.DataFrame(data=data[1:,0:],
                  columns=data[0,0:])