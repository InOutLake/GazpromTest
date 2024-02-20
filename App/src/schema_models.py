from pydantic import BaseModel, Field

class CreateData(BaseModel):
    device_id: int
    x: float
    y: float
    z: float