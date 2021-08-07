
from flask import Flask, render_template, url_for,request
from sklearn.linear_model import LinearRegression
import joblib
import pandas
import numpy as np


app = Flask(__name__)


db = pandas.read_csv("marks.csv")
X = db["hours"]
X = X.values
X = X.reshape(4,1)
y = db["marks"]

mind = LinearRegression()
mind.fit(X,y)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        data = np.array(data).reshape(-1,1)
        
        my_prediction = mind.predict(data)
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)





