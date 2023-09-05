import requests

data = {
    'data': 'TextToPredict'
}

headers = {'ngrok-skip-browser-warning': 'true'}  

response = requests.post('YourNgrokURL.ngrok-free.app/predict', json=data, headers=headers)

if response.status_code == 200:
    try:
        result = response.json()
        print('Prediction:', result['prediction'])
    except ValueError:
        print('Response does not contain valid JSON data.')
else:
    print('Error:', response.status_code)
