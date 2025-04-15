CREATE SCHEMA IF NOT EXISTS globa_kutsenko;

CREATE TABLE IF NOT EXISTS globa_kutsenko.drivers (
 driver_id INTEGER PRIMARY KEY,
 name TEXT,
 rating FLOAT
);

CREATE TABLE IF NOT EXISTS globa_kutsenko.cars (
 car_id INTEGER PRIMARY KEY,
 model TEXT,
 color TEXT
);

CREATE TABLE IF NOT EXISTS globa_kutsenko.customers (
 customer_id INTEGER PRIMARY KEY,
 rating INTEGER 
);

CREATE TABLE IF NOT EXISTS orders (
 start_adress TEXT,
 end_adress TEXT,
 orderTime TIMESTAMP, 
 driver_id INTEGER,
 car_id INTEGER,
 customer_id INTEGER,
 FOREIGN KEY (driver_id) REFERENCES globa_kutsenko.drivers(driver_id),
 FOREIGN KEY (car_id) REFERENCES globa_kutsenko.cars(car_id),
 FOREIGN KEY (customer_id) REFERENCES globa_kutsenko.customers(customer_id),
 status TEXT
);
