#!/usr/bin/env python
# coding: utf-8

# Prediction of the value of a car based on its characteristics

## Data extraction

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge

import pickle

cars_df = pd.read_csv("code_for_data_extraction/cars_infos_creditas.csv", encoding="utf-8")

columns = ["car_description", "car_name"]
for col in columns:
    cars_df[col] = cars_df[col].str.replace(" ", "_").str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

cars_df["value"] = cars_df["value"].str.replace(u'\xa0', u'', regex=True)
cars_df["value"] = cars_df["value"].str.replace('R$', '', regex=False)
cars_df["value"] = cars_df["value"].astype('float64')

cars_df["car_name"] = cars_df["car_name"].astype("category")
cars_df["car_description"] = cars_df["car_description"].astype("category")
cars_df["year"] = cars_df["year"].astype("category")

cars_df["value"] = np.log1p(cars_df["value"])

## Feature engineering

car_description_lst = cars_df["car_description"].str.split("_").to_list()
car_desc = []
for item in car_description_lst:
    car_desc.append(item[-1])
    
cars_df["car_desc"] = car_desc

cars_df2 = cars_df.copy()
cars_df2 = cars_df2.drop(labels=["car_description"], axis=1)

## Model

full_train_df, test_df = train_test_split(cars_df2, test_size=0.2, random_state=15)

y_full_train = full_train_df["value"].values

del full_train_df["value"]

full_train_df = full_train_df.reset_index(drop=True) 
full_train_dict = full_train_df.to_dict(orient="records")
dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(full_train_dict)

# Ridge
ridge = Ridge(alpha=1.919193, random_state=1)
ridge.fit(X_full_train, y_full_train)

with open('model.bin', 'wb') as f_out:
   pickle.dump((dv, ridge), f_out)
f_out.close() ## After opening any file it's nessecery to close it







