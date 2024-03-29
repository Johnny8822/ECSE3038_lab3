from fastapi import FastAPI, Request,   Response, status, HTTPException

import uuid
app = FastAPI()

tanks = [] 


@app.get("/tank")
def get_tank():  
    return tanks 


@app.get("/tank/{id}")
async def get_tankid(id:str):
    for i in tanks:
        if i["id"]==id:
            return i
        raise HTTPException(status_code=404, detail="Invalid ID ")



@app.post("/tank")
async def post_tank(request: Request, response: Response):   
    tank = await request.json()

    new_uuid = uuid.uuid4()

    id = str(new_uuid)
    tank = {"id": id, **tank}

    tanks.append(tank)
    response.status_code = status.HTTP_201_CREATED

    return(tank)




@app.patch("/tank/{id}", status_code=status.HTTP_200_OK)
async def change_tanks(id:str, request: Request):
    change_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            change_tank.pop("id",None)
            tanks[i] = {**tank, **change_tank}
            return tanks[i]
        raise HTTPException(status_code=404, detail="Object not found")



@app.delete("/tank/{id}", status_code=status.HTTP_200_OK)
def remove_tank(id:str):
    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
           del tanks[i]
           return()
    raise HTTPException(status_code=404, detail="Object not found")
