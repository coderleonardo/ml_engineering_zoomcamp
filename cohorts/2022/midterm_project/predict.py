import pickle
import pandas as pd
import numpy as np

model_file = 'model/model.bin'
with open(model_file, 'rb') as f_in: ## Note that never open a binary file you do not trust!
    dv, model = pickle.load(f_in) # dict_vectorizer, model
f_in.close()

def pipeline(initial_df):
    """
    This function implements all data processing and feature engineering in order
    to return a final treated dataframe ready to be used as model input.
    
    Input: Dataframe (initial dataframe)
    
    Return: X (data to be used as input in our model)
    
    Example of the initial dataframe:
        car_description 	      car_name 	       km_traveled 	  year
    1.6 16v Advance Xtronic 	  Nissan Versa     6.214 	      2022
    2.0 Lx 4x2 16v Automático 	  Honda Crv 	   102.064        2012
    1.8 Gli 16v Automático 	      Toyota Corolla   35.990 	      2019
    1.6 Freestyle 16v Powershift  Ford Ecosport    51.683 	      2017
    1.6 16v Flexstart S Xtronic   Nissan Kicks 	   41.417 	      2018
    
    Type of each column of the initial dataframe:
        car_description: object
        car_name: object
        km_traveled: float64
        year: int64
    
    """
    
    cars_df = initial_df.copy()
    
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
    
    return X


raw_data = [("1.6 16v Advance Xtronic", "Nissan Versa", 6.214, 2022),
           ("1.8 Gli 16v Automático", "Toyota Corolla", 35.990, 2019), 
           ("Freestyle 16v Powershift", "Ford Ecosport", 51.683, 2017)]
df = pd.DataFrame(raw_data, 
                 columns=["car_description", "car_name", "km_traveled", "year"])
X = pipeline(df)

def predict(X):
    y_pred = np.expm1(model.predict(X))
    
    return y_pred

y_predict = predict(X)
print(y_predict)