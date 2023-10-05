import requests

data = {
    'data': 'Your text goes here. Is this a spam message?'
} 

response = requests.post('http://localhost:5000/predict', json=data)

if response.status_code == 200:
    try:
        result = response.json()
        print('Prediction:', result['prediction'])
    except ValueError:
        print('Response does not contain valid JSON data.')
else:
    print('Error:', response.status_code)
