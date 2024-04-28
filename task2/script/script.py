import requests
import os
from datetime import datetime
import time

url = os.getenv('SERVICE_URL') + '/statistics'

while True:
    response = requests.get(url)
    count = response.text

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time}: {count}\n"

    with open('statistics.log', 'a') as file:
        file.write(log_entry)

    time.sleep(5)
