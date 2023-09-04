import requests

data = {
    'data': 'SMS to 32749 for collecting your cash prize of $1000'
}

headers = {'ngrok-skip-browser-warning': 'true'}  

response = requests.post('https://acf3-2a02-ce0-3800-883-2d31-74eb-dae5-f23.ngrok-free.app/predict', json=data, headers=headers)

if response.status_code == 200:
    try:
        result = response.json()
        print('Prediction:', result['prediction'])
    except ValueError:
        print('Response does not contain valid JSON data.')
else:
    print('Error:', response.status_code)
