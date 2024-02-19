from fastapi import FastAPI, Request,   Response, status 

import uuid
app = FastAPI()

tanks = [] 


@app.get("/tank")
def get_tank():  
    return tanks 


@app.get("/tank{tank_id}") 
def get_tank_id(): 
     tank_num = 0 
#    for j in range (len(tanks)):
    



@app.post("/tank") 
async def post_tank(request: Request, response: Response):
   tank = await request.json 
   new_uuid = uuid.uuid4() 
   
   tank = {"id": str(new_uuid), **tank}
   tanks.append(tank)  
   response.status_code  = status.HTTP_201_CREATED
   return(tank)


@app.patch("/tank/{id}")
async def patch_tank(id: str, request:Request):
    patched_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            tanks[i] = {**tank, **patched_tank}
            return tanks[i]