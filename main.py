from fastapi import FastAPI

app = FastAPI()


@app.get("/GIRSU")
async def root():
    return {"GIRSU": "Gestion Integral De Residuos Solidos Urbanos :"

      "Es una estrategia transversal, en articulación con provincias y municipios, que promueve el saneamiento ambiental" 
      "y la optimización de recursos para garantizar una gestión moderna y eficiente de los residuos sólidos urbanos,"
      "bajo el paradigma de la economía circular." 
      "Fomentando a la separación en origen, el reciclado, la reutilización y la valorización de los residuos para convertirlos en "
      "insumos de los procesos productivos."
      "Aprendamos a consumir y generar residuos con conciencia"}
    

@app.get("/componentes-de-tu-basura/")
async def Lista():
    return {"1":"metales", "2":"Carton", "3":"plasticos", "4":"vidrios", "5":"organicos","6":"Otros",

    "Importante" : "Para reciclar es necesario preclasificar en tu domicilio"}

@app.get("/cantidad-de-residuos-generados-en-tu-localidad/")
async def read_item(poblacion:int,CteResiduosHab:float):
    CantidadResiduos=poblacion*CteResiduosHab
    return {"CantidadResiduos": CantidadResiduos,"poblacion":poblacion,"CteResiduosHab":CteResiduosHab,
    CantidadResiduos: "kg de basura son producidos diariamente en tu localidad",
    "mensaje" : "si no se aplica una gestión a estos residuos, terminan en un sitio de disposición final,"
    "probablemente un basural a cielo abierto, donde no solo no va a volver a la economía, sino que se genera un"
    "foco contaminante donde abundan vectores transmisores de enfermedades, se producen lixiviados y se quema la "
    "basura para reducir el volumen, generando nuevos contaminantes gaseosos"}


@app.get("/aplicando-GIRSU-es-posible-reciclar-en-tu-localidad-esta-cantidad/")
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
        Vidrios = CantidadResiduos * .041
        Precio_Vidrio_04_22 = 6
        Ganancia_anual_vidrio = Vidrios * Precio_Vidrio_04_22 * 365
        return {"ganancia_anual":Ganancia_anual_vidrio,"tipo_de_material":"vidrios"}
    if tipoMaterial == 5: 
        organicos = CantidadResiduos * .51
        Ganancia_anual_organicos = "El compost es un abono lleno de nutrientes que nos sirve para mejorar el suelo de nuestro jardín o abonar nuestras plantas, una alternativa más respetuosa con el medio ambiente que los fertilizantes químicos."
        return {"ganancia_anual":Ganancia_anual_organicos,"tipo_de_material":"organicos"}
    if tipoMaterial == 6: 
        otros = CantidadResiduos * .15
        Ganancia_anual_otros = "El 15 '%' de los residuos que generamos no es posible reciclarlos de manera directa, sin realizar procesos fisico-quimicos para volver a obtener la materia prima pura"
        return {"ganancia_anual":Ganancia_anual_otros,"tipo_de_material":"otros"}
        
    return {"error":"tipo de material invalido"}


@app.get("/Informacion/")
async def read_info(tipoMaterial:int):
    if tipoMaterial == 0:
        Info_general = "porcentajes de residuos domiciliarios ponderados según nación"
        return {
            "info":Info_general,
            "porcentaje_residuos":[{"Metales":2},{"CartonYPapel":15},{"plasticos":13},{"vidrios":4},{"Organico":51},{"otros":15}]
        }


    if tipoMaterial == 1:
        Info_Metal = "se estima que el 2 '%' de nuestros residuos corresponde a metales, los cuales son de fácil separación en origen y pueden ser reciclados, teniendo además un alto valor de reventa"
        return {
            "info":Info_Metal,
            "porcentaje_residuos":[{"Metales":2}]
        }
    if tipoMaterial == 2: 
        Info_CartonYPapel = "se estima que un 15 '%' de nuestros residuos esta en este grupo, una vez separado, es necesario compactarlo y enfardarlo para después venderlo"
        return {
            "info":Info_CartonYPapel,
            "porcentaje_residuos":[{"CartonYPapel":15}]
        }
    if tipoMaterial == 3:
        Info_plasticos = "Se estima que un 13 '%' de nuestros residuos son plásticos, los cuales al ser incinerados son los principales formadores de dioxinas y furanos sustancias altamente cancerígenas, reciclandolos se obtiene un beneficio económico y se evita la generación de contaminantes secundarios, para reciclarlos es necesario además de la separación en origen clasificarlos en PET, PVC, PEAD, PEBD, y además clasificarlos según el color"
        return {
            "info":Info_plasticos,
            "porcentaje_residuos":[{"plasticos":13}]
            }
    if tipoMaterial == 4: 
        Info_vidrios = "Aproximadamente un 4 porciento de lo que descartamos son vidrios, siendo este material el más fácil de recilcar siempre que exista una preclasificación en origen"
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
    