import requests
from datetime import datetime
import random
from config import API_HOST
from helpers import generate_value

device_id = 1
for i in range(50):
    random.seed(datetime.now().microsecond)
    data = {
        'device_id': device_id,
        'x': generate_value(),
        'y': generate_value(),
        'z': generate_value()
    }
    response = requests.post(f"{API_HOST}/data/", json=data)