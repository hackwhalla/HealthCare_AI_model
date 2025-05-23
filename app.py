"""import requests
url = 'http://127.0.0.1:5000/predict'
data  = {"disease_name": "Fever"}
response = requests.post(url,json=data)
print(response)
x = response.json()
print(x)
print(x['Ayurvedic_medicin'])
print(x['Exerise'])
print(x['Home_remedies'])"""
from disease_solution import app

if __name__ == "__main__":
    app.run(debug=True)