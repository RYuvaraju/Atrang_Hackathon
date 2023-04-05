from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('heartdis.sav', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('heart disease.html')


@app.route('/Predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    arr = np.array([[data1, data2, data3, data4, data5, data6]])
    pred = model.predict(arr)
    return render_template('hafter.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)