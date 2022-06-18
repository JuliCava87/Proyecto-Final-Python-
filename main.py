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
    return {"1":"metales", "2":"Carton", "3":"plasticos", "4":"vidrios", "5":"organicos","6":"Otros"}

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
    if tipoMaterial == 5: 
        organicos = CantidadResiduosDia * .51
        Ganancia_anual_organicos = "El compost es un abono lleno de nutrientes que nos sirve para mejorar el suelo de nuestro jardín o abonar nuestras plantas, una alternativa más respetuosa con el medio ambiente que los fertilizantes químicos."
        return {"ganancia_anual":Ganancia_anual_organicos,"tipo_de_material":"organicos"}

        
    return {"error":"tipo de material invalido"}


@app.get("/Informacion/")
async def read_info(tipoMaterial:int):
    if tipoMaterial == 0:
        Info_general = "IIIINFO GLOBAL"
        return {
            "info":Info_general,
            "porcentaje_residuos":[{"Metales":2},{"CartonYPapel":15},{"plasticos":13},{"vidrios":4},{"Organico":51},{"otros":15}]
        }


    if tipoMaterial == 1:
        Info_Metal = "se estima que en los BCA, casi el 2 '%' corresponde a metales, los cuales son de fácil separación en origen y pueden ser reciclados, teniendo además un alto valor de reventa"
        return {
            "info":Info_Metal,
            "porcentaje_residuos":[{"Metales":2}]
        }
    if tipoMaterial == 2: 
        Info_CartonYPapel = "se estima que en los BCA un 15 '%' corresponde a este tipo de materiales, es necesario compactarlo y enfardarlo para después venderlo"
        return {
            "info":Info_CartonYPapel,
            "porcentaje_residuos":[{"CartonYPapel":15}]
        }
    if tipoMaterial == 3:
        Info_plasticos = "Se estima que en los BCA un 13 porciento corresponde a plásticos, los cuales al ser incinerados son los principales formadores de dioxinas y furanos, reciclandolos no solo se obtiene un beneficio económico, sino que se previene este contaminante cuando existe la quema de residuos"
        return {
            "info":Info_plasticos,
            "porcentaje_residuos":[{"plasticos":13}]
            }
    if tipoMaterial == 4: 
        Info_vidrios = "se estima que en los BCA un 4 porciento son vidrios, son fáciles de reciclar"
        return {
            "info":Info_vidrios,
            "porcentaje_residuos":[{"vidrios":4}]
            }

    if tipoMaterial == 5: 
        Info_Organicos = "se estima que un 51'%' de los residuos domiciliarios son orgánicos, resaltando en este número la importancia de realizar compostaje"
        return {
            "info":Info_Organicos,
            "porcentaje_residuos":[{"Organico":51}]
            }

    if tipoMaterial == 6: 
        Info_Otros = "se estima que un 15'%' de los residuos domiciliarios son corresponden a esta categoría, en la que no se podría reciclar sin tratamiento previo para recuperar la materia incial, o no existen puntos de recolección y compra de la materia prima"
        return {
            "info":Info_Otros,
            "porcentaje_residuos":[{"Otros":15}]
            }            
    #  devolver info reelevante respecto a porcentaje de residuos a nivel nación
    # return {"alert":"metodo en construccion" }