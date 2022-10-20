# to run bentoml -> bentoml serve service.py:svc --reload
import bentoml

from bentoml.io import JSON

# create a runner from the saved Booster
model_ref = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_ref.custom_objects["dictVectorizer"]

model_runner = model_ref.to_runner()

# create a BentoML service
svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])

# define a new endpoint on the BentoML service
@svc.api(input=JSON(), output=JSON())
def classify(application_data):

    vector = dv.transform(application_data)

    prediction = model_runner.predict.run(vector)
    
    print(prediction)
    
    result = prediction[0]
    
    if result > 0.5:
        return { "status": "DECLINED" }
    elif result > 0.23:
        return { "status": "MAYBE" }
    else:
        return { "status": "APPROVED"}
    
