import pickle
import numpy as np

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_proba = model.predict_proba(X)[:, 1]
    return y_proba[0]

with open("model2.bin", "rb") as f_in:
    model = pickle.load(f_in)

with open("dv.bin", "rb") as f_in:
    dv = pickle.load(f_in)


app = Flask("bank_credit_scoring")


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    prediction = predict_single(customer, dv, model)
    scoring = prediction >= 0.5
    
    result = {
        "scoring_probability": float(prediction),
        "scoring": bool(scoring),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)