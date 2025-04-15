from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from config import connect

from random import randint


router = APIRouter(prefix="/api/v1")

class Driver(BaseModel):
    name: str
    rating: float

@router.post("/drivers/create")
async def create_driver(driver: Driver):
    
    cur = connect.cursor()
    
    id = randint(1, 999999)
    
    query = """INSERT INTO globa_kutsenko.drivers (driver_id, name, rating)
    VALUES (%s, %s, %s);"""
    
    values = (id, driver.name, driver.rating)
    
    cur.execute(query, values)
    
    return JSONResponse(status_code=200, content={"message": "Driver created successfully"})