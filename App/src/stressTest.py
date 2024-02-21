from locust import HttpUser, task
from helpers import generate_value
import random

class SendingDataUser(HttpUser):
    @task
    def index(self):
        data = {
            'device_id': random.randint(1, 10),
            'x': generate_value(),
            'y': generate_value(),
            'z': generate_value()
        }
        self.client.post("/data/", data=data)

class RequestingStatisticsUser(HttpUser):
    @task
    def index(self):
        data = {
            'device_id': random.randint(1, 10),
        }
        self.client.get("/statistic/", data=data)