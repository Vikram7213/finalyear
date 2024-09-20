import requests
import json
from concurrent.futures import ThreadPoolExecutor

# Define the URL for your NodePort service
url = 'http://localhost:31808/predict'

# Define the payload (the data you want to send)
payload = [
    {
        "PM2.5": 81.4,
        "PM10": 124.5,
        "NO": 1.44,
        "NO2": 20.5,
        "NOx": 12.08,
        "NH3": 10.72,
        "CO": 0.12,
        "SO2": 15.24,
        "O3": 127.09,
        "Benzene": 0.2,
        "Toluene": 6.5,
        "Xylene": 0.06,
        "AQI": 184.0
    }
]

# Function to send a POST request
def send_request():
    response = requests.post(url, json=payload)
    return response.json()

# Send multiple requests concurrently
with ThreadPoolExecutor(max_workers=9) as executor:
    futures = [executor.submit(send_request) for _ in range(100)]
    results = [f.result() for f in futures]

# Print the responses
for result in results:
    print(result)
