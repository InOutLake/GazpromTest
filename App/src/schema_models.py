from pydantic import BaseModel
from datetime import datetime
from pytz import timezone
from .config import TIMEZONE

class CreateData(BaseModel):
    device_id: int
    x: float
    y: float
    z: float

class Statistic(BaseModel):
    maxval: bool = True
    minval: bool = True
    median: bool = True
    summ: bool = True
    count: bool = True
    start_time: datetime = datetime(year=2024, month=2, day=19, tzinfo=timezone(TIMEZONE))
    end_time: datetime = datetime.now(timezone(TIMEZONE))
