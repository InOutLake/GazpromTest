from sqlalchemy.orm import Session
from models import *

def device_exists(db: Session, device_id: int):
    device = db.query(Device).filter(Device.device_id == device_id).first()
    return device is not None