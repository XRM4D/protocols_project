from fastapi import FastAPI
import uvicorn

from api import router

from config import connect

app = FastAPI()

if __name__ == '__main__':
    
    connect.autocommit = True
    
    cur = connect.cursor()
    
    with open('migrate.sql', 'r') as f:
        sql_new = f.read()
        
    cur.execute(sql_new)
    
    app.include_router(router)
        
    uvicorn.run(app, host="0.0.0.0", port=8080)