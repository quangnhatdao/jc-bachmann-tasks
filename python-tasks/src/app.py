from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import json
import plotly
import plotly.express as px
import requests

app = Flask(__name__)

"""
handler for index route
"""
@app.route("/")
def index_handler():
    return render_template('index.html')

"""
handler for data route
"""
@app.route("/data")
def data_handler():
    # convert data frame to json
    return get_df().to_json(orient='records')

"""
method for generating data frame
""" 
def get_df():

    # initialize data array matrix
    data = np.array([['a','b']])
    
    # fill it with a and b values
    for x in range(1000):
        a = np.random.randint(101, size=1)[0]
        b = a % 10
        data = np.append(data, [[a, b]], axis=0)
 
    # return data frame
    return pd.DataFrame(data=data[1:,0:],
                  columns=data[0,0:])