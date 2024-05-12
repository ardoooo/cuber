import requests
import os
from datetime import datetime
import time

url = os.getenv('SERVICE_URL') + '/statistics'
sleep_per_s = int(os.getenv('INNER_INTERVAL_S'))

log_directory = 'logs'
os.makedirs(log_directory, exist_ok=True)
log_file_path = os.path.join(log_directory, 'statistics.log')

while True:
    response = requests.get(url)
    count = response.text

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time}: {count}\n"

    with open(log_file_path, 'a') as file:
        file.write(log_entry)

    time.sleep(sleep_per_s)
