from sqlalchemy.orm import Session
from models import *
from datetime import datetime
import random

def device_exists(db: Session, device_id: int):
    device = db.query(Device).filter(Device.device_id == device_id).first()
    return device is not None

def generate_value():
    random.seed(datetime.now())
    return random.random() * random.randint(-5, 5)