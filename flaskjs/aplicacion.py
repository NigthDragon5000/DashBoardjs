# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:15:02 2020

@author: JAIR
"""

from flask import Flask, Markup, render_template
import pandas as pd

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
    

base=pd.DataFrame()
base['month']=labels
base['values']=values


@app.route('/')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('chart.html', title='Bitcoin Monthly Price in USD',\
                           max=17000, labels=bar_labels, values=bar_values,\
                           titles=base.columns.values,\
                           tables=[base.to_html(classes='data')],\
                           set=zip(values, labels, colors)    )

 
if __name__ == "__main__":
    app.run(debug=False)
    