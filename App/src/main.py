from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from .models import Device, Data
from .schema_models import *
from .helpers import *
from . import statistic_calculations as sc
from typing import List


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

@app.post('/data/', response_model=CreateData)
async def create_data(data: CreateData):
    new_data = Data(**data.model_dump())
    if not device_exists(db, new_data.device_id):
        raise HTTPException(status_code=404, detail='Device with such ID is not registered')
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


@app.get('/statistic/')
async def statistic(
            device_id: int,
            max_value: bool = True, 
            min_value: bool = True, 
            median: bool = True, 
            sum: bool = True, 
            count: bool = True, 
            start_time: datetime = datetime(year=2024, month=2, day=19, tzinfo=timezone(TIMEZONE)), 
            end_time: datetime = datetime.now(timezone(TIMEZONE))
        ):
    
    if not device_exists(db, device_id):
        raise HTTPException(status_code=404, detail='Device with such ID is not registered')
    
    data = db.query(Data).\
                filter(
                    Data.device_id == device_id,
                    Data.recieve_timestamp > start_time,
                    Data.recieve_timestamp < end_time
                ).\
                with_entities(Data.x, Data.y, Data.z)\
                .all()
    
    if not data:
        raise HTTPException(status_code=404, detail=f'Data from device with id={device_id} have not been found')

    statistics = {}
    statistic_functions = {
        'max_value': sc.max_values,
        'min_value': sc.min_values,
        'median': sc.medians,
        'sum': sc.summs,
        'count': sc.counts
    }
    for key, func in statistic_functions.items():
        if locals()[key]:
            result = func(data)
            statistics.setdefault(key, result)
    return statistics

if __name__ == '__main__': 
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
