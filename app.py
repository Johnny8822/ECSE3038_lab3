from fastapi import FastAPI, Request,   Response, status 

app = FastAPI()

tanks = [] 


@app.get("/tank")
def get_tank():  
    return tanks 


@app.get("/tank{tank_id}") 
def get_tank_id(): 
   tank_num = 0 
   for j in range len(tanks)