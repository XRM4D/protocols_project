from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import engine
from sqlalchemy import text
from databases.Car import Car 

metadata = MetaData(schema='globa_kutsenko')
Base = declarative_base(metadata=metadata)

def init_schema():
    with engine.connect() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS globa_kutsenko"))
        connection.commit()
    Base.metadata.create_all(engine)