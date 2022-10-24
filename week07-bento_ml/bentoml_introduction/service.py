# to run bentoml -> bentoml serve service.py:svc --reload
# to run bentoml in productio with docker:
    # docker run -it --rm -p 3000:3000 credit_risk_classifier:hash... serve --production
import bentoml

from bentoml.io import JSON
from bentoml.io import NumpyNdarray # to validate the data

from pydantic import BaseModel

# define the schema of the input data
class CredictApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int 
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: float
    price: float

# create a runner from the saved Booster
model_ref = bentoml.xgboost.get("credit_risk_model:z5zswdctcgqzmh6i")
dv = model_ref.custom_objects["dictVectorizer"]

model_runner = model_ref.to_runner()

# create a BentoML service
svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])

# define a new endpoint on the BentoML service
# @svc.api(input=NumpyNdarray(shape=(-1, 29), enforce_shape=True), output=JSON())
@svc.api(input=JSON(), output=JSON())
async def classify(application_data):

    #application_data = credict_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    
    print(prediction)
    
    result = prediction[0]
    
    if result > 0.5:
        return { "status": "DECLINED" }
    elif result > 0.23:
        return { "status": "MAYBE" }
    else:
        return { "status": "APPROVED"}
    
