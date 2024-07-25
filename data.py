import requests

url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url, params=parameters)
data = response.json()
question_data = data["results"]
