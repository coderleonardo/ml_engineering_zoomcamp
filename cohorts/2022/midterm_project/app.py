import pickle
import pandas as pd
import numpy as np

import json
from flask import Flask
from flask import request
from flask import render_template

# create an app object using the Flask class
app = Flask(__name__, template_folder='templates')

model_file = 'model.bin'
with open(model_file, 'rb') as f_in: ## Note that never open a binary file you do not trust!
    dv, model = pickle.load(f_in) # dict_vectorizer, model
f_in.close()

# define the route to be home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    This function implements all data processing and feature engineering in order
    to return a final treated dataframe ready to be used as model input and make the 
    prediction.
    
    Input: JSON (to be pass as a dataframe)
    
    Return: y predict
    
    Example of the initial JSON:
        {
            "car_description": "1.6 Freestyle 16v Powershift", 
            "car_name": "Ford Ecosport",
            "km_traveled": "51.683"
            "year": "2017"
        }
    
    Type of each key of the initial JSON:
        car_description: object
        car_name: object
        km_traveled: object
        year: object
    
    """
    
    cars_df = pd.DataFrame(request.form.to_dict(flat=False))

    cars_df["km_traveled"] = cars_df["km_traveled"].astype("float64")
    cars_df["year"] = cars_df["year"].astype("int64")
    
    columns = ["car_description", "car_name"]
    for col in columns:
        cars_df[col] = cars_df[col].str.replace(" ", "_").str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    cars_df["car_name"] = cars_df["car_name"].astype("category")
    cars_df["car_description"] = cars_df["car_description"].astype("category")
    cars_df["year"] = cars_df["year"].astype("category")
        
    car_description_lst = cars_df["car_description"].str.split("_").to_list()
    car_desc = []
    for item in car_description_lst:
        car_desc.append(item[-1])

    cars_df["car_desc"] = car_desc
    
    cars_df = cars_df.drop(labels=["car_description"], axis=1)
            
    X = dv.transform(cars_df.reset_index(drop=True).to_dict(orient="records"))

    y_pred = np.expm1(model.predict(X))[0]
    

    return render_template('index.html',
                            prediction_text='The value of the car is R${}.'\
                                .format(round(y_pred, 3)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9696)