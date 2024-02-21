import requests
from datetime import datetime
import random
from config import API_HOST

device_id = 1
for i in range(50):
    random.seed(datetime.now().microsecond)
    data = {
        'device_id': device_id,
        'x': random.random()*random.randint(-10, 100),
        'y': random.random()*random.randint(-10, 100),
        'z': random.random()*random.randint(-10, 100)
    }
    response = requests.post(f"{API_HOST}/data/", json=data)