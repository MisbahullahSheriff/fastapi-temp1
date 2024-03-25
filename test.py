import json
import requests

url = "https://fastapi-temp1.onrender.com/predict"

x_new = dict(
	company="Ford",
	year=2018,
	owner="First",
	fuel="Diesel",
	km_driven=90000,
	mileage_mpg=54.06,
	engine_cc=1498.0,
	seats=5.0
)
x_new_json = json.dumps(x_new)

response = requests.post(url, data=x_new_json)

print(response.text)