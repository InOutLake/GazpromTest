# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Device(Base):
    __tablename__ = 'Device'

    device_id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"Device_device_id_seq\"'::regclass)"))


class Datum(Base):
    __tablename__ = 'Data'

    device_id = Column(ForeignKey('Device.device_id', onupdate='CASCADE'), primary_key=True, nullable=False)
    recieve_timestamp = Column(DateTime, primary_key=True, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)

    device = relationship('Device')
