from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bienvenido a mi sistema"}

@app.get("/cantidad-de-residuos/")
async def read_item(poblacion:int,CteResiduosHab:int):
    CantidadResiduos=poblacion*CteResiduosHab
    return {"CantidadResiduos": CantidadResiduos,"poblacion":poblacion,"CteResiduosHab":CteResiduosHab}

@app.get("/tipo-material/")
async def Lista():
    return {"1":"metales", "2":"Carton", "3":"plasticos", "4":"vidrios"}

@app.get("/cantidad-posible-reciclar/")
async def read_item(CantidadResiduos:int,tipoMaterial:int):
    if tipoMaterial == 1:
        Precio_Metal = 18
        Metales = CantidadResiduos * 0.018
        Ganancia_anual_Metal = Metales * Precio_Metal * 365
        return {"ganancia_anual":Ganancia_anual_Metal,"tipo_de_material":"metales"}
    if tipoMaterial == 2: 
        CartonYPapel = CantidadResiduos * 0.151
        Precio_CartonYPapel_04_22 = 12
        Ganancia_anual_Carton = CartonYPapel * Precio_CartonYPapel_04_22 * 365
        return {"ganancia_anual":Ganancia_anual_Carton,"tipo_de_material":"carton"}
    if tipoMaterial == 3:
        Plasticos = CantidadResiduos * .132
        Precio_Plastico_04_22 = 6
        Ganancia_anual_plastico = Plasticos * Precio_Plastico_04_22 * 365
        return {"ganancia_anual":Ganancia_anual_plastico,"tipo_de_material":"plasticos"}
    if tipoMaterial == 4: 
        Vidrios = CantidadResiduosDia * .041
        Precio_Vidrio_04_22 = 6
        Ganancia_anual_vidrio = Vidrios * Precio_Vidrio_04_22 * 365
        return {"ganancia_anual":Ganancia_anual_vidrio,"tipo_de_material":"vidrios"}
    return {"error":"tipo de material invalido"}

    menu = int(input( 'seleccione que desea reciclar, 1. Metales 2. CartonYPapel 3. Plasticos 4.Vidrios\n'))