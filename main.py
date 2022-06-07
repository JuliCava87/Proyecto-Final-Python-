from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/cantidad-de-residuos/")
async def read_item(poblacion:int,CteResiduosHab:int):
    CantidadResiduos=poblacion*CteResiduosHab
    return {"CantidadResiduos": CantidadResiduos,"poblacion":poblacion,"CteResiduosHab":CteResiduosHab}


