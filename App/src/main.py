from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import Device, Data
from .schema_models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = Session()

app = FastAPI()
app.title = 'app'

@app.post('/device/')
async def create_device():
    new_device = Device()
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

@app.get('/data/{device_id}')
async def device_data(device_id: int):
    device = db.query(Device).filter(Device.device_id == device_id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    else:
        data = db.query(Data).filter(Data.device_id == device_id).limit(10).all()
    return {"device": device, "data": data}

@app.post('/data/', response_model=CreateData)
async def create_data(data=CreateData):
    return data

@app.get('/statistic/')
async def statistic(maxval: bool=True, minval: bool=True,
                            median: bool=True): #TODO add time
    return {'message': 'all calculations will be here'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

