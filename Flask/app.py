# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:26:44 2020

@author: Ritesh
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Chance of Admit.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/y_pred',methods=['POST'])
def y_pred():
    '''
    For rendering results on HTML GUI
    '''
    grescore         =request.form['grescore']
    tofelscore       =request.form['tofelscore']
    universityrating =request.form['universityrating']
    sop              =request.form['sop']
    lor              =request.form['lor']
    cgpa             =request.form['cgpa']
    research         =request.form['research'] 
    data=[[int(grescore),int(tofelscore),int(universityrating),float(sop),float(lor),float(cgpa),int(research)]]
    prediction  = model.predict(data)
    print(prediction)
    output=prediction[0][0]
    return render_template('base.html', prediction_text=output)
   

if __name__ == "__main__":
    app.run(debug=True)
