import requests
import json

#api endpoint
api_url = "https://tuftsctsi.github.io/C2D2AI/predict"

payload = {
    "age": 65,
    "sex": "female",
    "covert_brain_infarction": False,
    "white_matter_disease": True,
    "white_matter_severity": "moderate",
    "prior_stroke": False,
    "prior_dementia": False
}

response = requests.post(api_url, json=payload)


print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")