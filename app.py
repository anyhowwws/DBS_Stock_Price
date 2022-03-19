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
        model = load("/Users/hows/Documents/Regression.joblib")
        pred = model.predict([[float(rates)]])
        s = "The predicted DBS share price is " + str(pred)
        return(render_template("index.html",results=s))
               
    else:
        return(render_template("index.html",results="2"))

if __name__=="__main__": #required if not in DEV env
    app.run()