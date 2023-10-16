- Data used:
    https://www.kaggle.com/datasets/kapturovalexander/bank-credit-scoring/

- Commands used:
    - To install pipenv: ```pip install "pipenv>2021.11.15,<2023.8.19"``` (See issue https://github.com/pypa/pipenv/issues/5927)
    - To install sklear==1.3.1: ```pipenv install numpy scikit-learn==1.3.1```

- pipenv version: 
    ```$ pipenv --version >>> pipenv, version 2023.7.23```

- First hash for sklearn:
    - sha256:0c275a06c5190c5ce00af0acbb61c06374087949f643ef32d355ece12c4db043

- Downloading the model:
```
PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2023/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```

- Using the model to make predictions:
```
# See https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/02-pickle.md

# Loading the model
with open("model1.bin", "rb") as f_in: # very important to use 'rb' here, it means read-binary 
    model = pickle.load(f_in)

with open("dv.bin", "rb") as f_in: # very important to use 'rb' here, it means read-binary 
    dict_vectorizer = pickle.load(f_in)

# Prediction
sample = {"job": "retired", "duration": 445, "poutcome": "success"}
X_sample = dict_vectorizer.transform(sample)

y_proba_sample = model.predict_proba(X_sample)[:, 1]
y_pred_sample = y_proba_sample >= 0.5

print(round(y_proba_sample[0], 3), y_pred_sample)
# Output: 0.902 [ True]
```

- Predicting the score:
```
import requests

url = "http://localhost:9696/predict"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
requests.post(url, json=client).json()
# Output: {'scoring': False, 'scoring_probability': 0.13968947052356817}
```

- Downloading the Docker image: ```docker pull svizor/zoomcamp-model:3.10.12-slim```

Infos about the image:
```
REPOSITORY              TAG            SIZE
svizor/zoomcamp-model   3.10.12-slim   147MB
```

- Testing the model with Docker
```
import requests

url = "http://0.0.0.0:9696/predict"

client = {"job": "retired", "duration": 445, "poutcome": "success"}
requests.post(url, json=client).json()
# Output: {'scoring': True, 'scoring_probability': 0.726936946355423}
```