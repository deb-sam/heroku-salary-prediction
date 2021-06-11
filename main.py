from flask import Flask,render_template,request
import joblib
import numpy as np

app= Flask(__name__)

#load a model
model=joblib.load('hiring_model.pkl')

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return 'Welcome to contact page'

@app.route('/predict',methods=['POST'])
def predict():
    exp=request.form.get('experience')
    score=request.form.get('test_score')
    I_score=request.form.get('Interview_score')
    prediction= model.predict([[exp,score,I_score]])
    output = round(prediction[0], 2)
    return render_template('base.html', prediction_text=f"Employee salary will be $ {output}")

app.run(debug=True)