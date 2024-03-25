import joblib
import pandas as pd
from fastapi import FastAPI
from car_data_model import Car

app = FastAPI(
    title="Car Price Prediction",
    description="This API will provide prediction of car prices for given set of specifications"
)


@app.get("/")
def index():
    return "Welcome to Car Price Prediction API using FastAPI"


@app.post("/predict")
def make_prediction(car: Car):
    x_new = pd.DataFrame(data=dict(
        company=[car.company],
        year=[car.year],
        owner=[car.owner],
        fuel=[car.fuel],
        km_driven=[car.km_driven],
        mileage_mpg=[car.mileage_mpg],
        engine_cc=[car.engine_cc],
        seats=[car.seats]
    ))
    model = joblib.load("model.joblib")
    predicted_value = model.predict(x_new)[0]
    return f"The car of given specifications will cost {predicted_value:,.0f} INR"