from fastapi import FastAPI
import time
from pydantic import BaseModel

class DeviceData(BaseModel):
    device_id: int
    x: float
    y: float
    z: float

app = FastAPI()

@app.get('/data/{device_id}')
async def device_data(device_id: int):
    return {'device_id': device_id}

@app.get('/staticstic/')
async def all_calculations(maxval: bool=True, minval: bool=True,
                            median: bool=True): #TODO add time
    return {'message': 'all calculations will be here'}

@app.post('/data/')
async def device_send_data(data: DeviceData):
    return data


