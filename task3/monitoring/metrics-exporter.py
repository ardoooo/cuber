from prometheus_client import start_http_server, Gauge
import requests
import time
import os

URL = os.getenv('SERVICE_URL') + '/statistics'
REQUEST_COUNT = Gauge('request_count', 'Total count of requests')

def fetch_statistics():
    response = requests.get(URL)
    return int(response.text)

def collect_metrics():
    count = fetch_statistics()
    REQUEST_COUNT.set(count)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        collect_metrics()
        time.sleep(30)
