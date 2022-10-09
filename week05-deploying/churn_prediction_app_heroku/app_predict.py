import pickle

import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

# create an app object using the Flask class
app = Flask('churn')

# load the trained model
model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in: # read binary
    dv, model = pickle.load(f_in)

# define the route to be home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    customer_dict = request.form.to_dict(flat=False)
    
    customer = {}
    for key, value in customer_dict.items():
        customer.update({key: value[0]})

    customer["tenure"] = int(customer["tenure"])
    customer["monthlycharges"] = float(customer["monthlycharges"])

    customer["totalcharges"] = customer["tenure"] * customer["monthlycharges"]

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    churn = y_pred >= 0.5

    result = {
        "churn_probability": float(y_pred),
        "churn": bool(churn)
    }

    
    return render_template('index.html', prediction_text='Churn probability is equal to {}. Churn? {}'.\
        format(round(result["churn_probability"], 3), result["churn"]))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
