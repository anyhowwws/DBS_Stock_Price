#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:34:21 2022

@author: hows
"""

from flask import Flask,request,render_template

from joblib import load
#Model = load("/Users/hows/Documents/Regression.joblib")
#Model.predict([[1.36]])

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        rates = request.form.get("rates")
        model = load("Regression.joblib")
        pred = model.predict([[float(rates)]])
        PRED=str(round(pred[0][0],2))
        s = "According to my humble prediction... DBS share price should be valued at: $" + PRED
        i = "Enter another amount above for another prediction!"
        return(render_template("index.html",results=s,instructions=i))
               
    else:
        defaultResults = ""
        defaultResponse = "Enter an amount above for an estimation!"
        return(render_template("index.html",results = defaultResponse ,instructions=defaultResults))

if __name__=="__main__": #required if not in DEV env
    app.run()
