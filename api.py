from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from config import connect

from random import randint


router = APIRouter(prefix="/api/v1")

class Driver(BaseModel):
    name: str
    rating: float

@router.post("/drivers")
async def create_driver(driver: Driver):
    
    cur = connect.cursor()
    
    id = randint(1, 999999)
    
    query = """INSERT INTO globa_kutsenko.drivers (driver_id, name, rating)
    VALUES (%s, %s, %s);"""
    
    values = (id, driver.name, driver.rating)
    
    cur.execute(query, values)
    
    return JSONResponse(status_code=200, content={"message": "Driver created successfully"})
    

@router.get("/drivers/all")
async def get_all_drivers():

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.drivers;"""

    cur.execute(query)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"drivers": res})
    
@router.get("/drivers/{driver_id}")
async def get_driver_by_id(driver_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.drivers WHERE driver_id = %s;"""

    values = (driver_id,)

    cur.execute(query, values)

    res = cur.fetchone()

    if not res:
        return JSONResponse(status_code=404, content={"message": "Driver not found"})

    return JSONResponse(status_code=200, content={"driver": res})
    

@router.delete("/drivers/{driver_id}")
async def delete_driver(driver_id: int):

    cur = connect.cursor()

    query = """DELETE FROM globa_kutsenko.drivers WHERE driver_id = %s;"""

    values = (driver_id,)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Driver deleted successfully"})

class Car(BaseModel):
    model: str
    color: str

@router.post("/cars")
async def create_car(car: Car):

    cur = connect.cursor()

    id = randint(1, 999999999)

    query = """INSERT INTO globa_kutsenko.cars (car_id, model, color)
    VALUES (%s, %s, %s);"""

    values = (id, car.model, car.color)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Car created successfully"})

@router.get("/cars/all")
async def get_all_cars():

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.cars;"""

    cur.execute(query)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"cars": res})
    

@router.get("/cars/{car_id}")
async def get_car_by_id(car_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.cars WHERE car_id = %s;"""

    values = (car_id,)

    cur.execute(query, values)

    res = cur.fetchone()

    if not res:
        return JSONResponse(status_code=404, content={"message": "Car not found"})

    return JSONResponse(status_code=200, content={"car": res})

@router.delete("/cars/{car_id}")
async def delete_car(car_id: int):

    cur = connect.cursor()

    query = """DELETE FROM globa_kutsenko.cars WHERE car_id = %s;"""

    values = (car_id,)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Car deleted successfully"})
    

class Customer(BaseModel):
    rating: float
    email: str

@router.post("/customers")
async def create_customer(customer: Customer):

    cur = connect.cursor()

    id = randint(1, 999999)

    query = """INSERT INTO globa_kutsenko.customers (customer_id, rating, email)
    VALUES (%s, %s, %s);"""

    values = (id, customer.rating, customer.email)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Customer created successfully"})

@router.get("/customers/all")
async def get_all_customers():

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.customers;"""

    cur.execute(query)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"customers": res})

@router.get("/customers/{customer_id}")
async def get_customer_by_id(customer_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.customers WHERE customer_id = %s;"""

    values = (customer_id,)

    cur.execute(query, values)

    res = cur.fetchone()

    if not res:
        return JSONResponse(status_code=404, content={"message": "Customer not found"})

    return JSONResponse(status_code=200, content={"customer": res})

@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):

    cur = connect.cursor()

    query = """DELETE FROM globa_kutsenko.customers WHERE customer_id = %s;"""

    values = (customer_id,)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Customer deleted successfully"})


class Order(BaseModel):
    start_adress: str
    end_adress: str
    driver_id: int
    car_id: int
    customer_id: int
    status: str = "pending"

@router.post("/orders")
async def create_order(order: Order):

    cur = connect.cursor()

    id = randint(1, 999999)

    query = """INSERT INTO globa_kutsenko.orders (order_id, start_adress, end_adress, orderTime, driver_id, car_id, customer_id, status)
    VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s);"""

    values = (id, order.start_adress, order.end_adress, order.driver_id, order.car_id, order.customer_id, order.status)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Order created successfully"})

@router.get("/orders/all")
async def get_all_orders():

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.orders;"""

    cur.execute(query)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"orders": res})

@router.get("/orders/{order_id}")
async def get_order_by_id(order_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.orders WHERE order_id = %s;"""

    values = (order_id,)

    cur.execute(query, values)

    res = cur.fetchone()

    if not res:
        return JSONResponse(status_code=404, content={"message": "Order not found"})

    return JSONResponse(status_code=200, content={"order": res})

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):

    cur = connect.cursor()

    query = """DELETE FROM globa_kutsenko.orders WHERE order_id = %s;"""

    values = (order_id,)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": "Order deleted successfully"})

class OrderStatus(BaseModel):
    status: str

@router.put("/orders/{order_id}/status")
async def update_order_status(order_id: int, order_status: OrderStatus):

    cur = connect.cursor()

    query = """UPDATE globa_kutsenko.orders SET status = %s WHERE order_id = %s;"""

    values = (order_status.status, order_id)

    cur.execute(query, values)

    return JSONResponse(status_code=200, content={"message": f"Order status updated to {order_status.status}"})

@router.get("/drivers/{driver_id}/orders")
async def get_driver_orders(driver_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.orders WHERE driver_id = %s;"""

    values = (driver_id,)

    cur.execute(query, values)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"orders": res})

@router.get("/customers/{customer_id}/orders")
async def get_customer_orders(customer_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.orders WHERE customer_id = %s;"""

    values = (customer_id,)

    cur.execute(query, values)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"orders": res})

@router.get("/cars/{car_id}/orders")
async def get_car_orders(car_id: int):

    cur = connect.cursor()

    query = """SELECT * FROM globa_kutsenko.orders WHERE car_id = %s;"""

    values = (car_id,)

    cur.execute(query, values)

    res = cur.fetchall()

    return JSONResponse(status_code=200, content={"orders": res})