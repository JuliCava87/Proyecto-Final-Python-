CteResiduosHabDia = 1.5
Poblacion = int(input('poblacion\n'))
CantidadResiduosDia = Poblacion * CteResiduosHabDia
Metales = float(CantidadResiduosDia * 0.018)
Precio_Metal_04_22 = 18
CartonYPapel = float(CantidadResiduosDia * 0.151)
Precio_CartonYPapel_04_22 = 12
Plasticos = float(CantidadResiduosDia * .132)
Precio_Plastico_04_22 = 6
Vidrios = float(CantidadResiduosDia * .041)
Precio_Vidrio_04_22 = 6
Organico = float(CantidadResiduosDia * .51)
Otros = float(CantidadResiduosDia * .148)
print ('En su localidad se emiten',CantidadResiduosDia,'Kg de residuos diarios')
print ('Aproximadamente la mitad de estos reciduos pueden ser reciclados, CUIDEMOS NUESTRO PLANETA')
menu = int(input( 'seleccione que desea reciclar, 1. Metales 2. CartonYPapel 3. Plasticos 4.Vidrios\n'))
if menu == 1:
    print ('En su localidad se generan', Metales,'Kg de metales diarios')
    Ganancia_anual_Metal = Metales * Precio_Metal_04_22 * 365
    print ('Reciclando los metales por un año, puede tener una ganancia de', Ganancia_anual_Metal, 'pesos')
if menu == 2: 
    print ('En su localidad se generan', CartonYPapel,'Kg de cartón diarios')
    Ganancia_anual_Carton = CartonYPapel * Precio_CartonYPapel_04_22 * 365
    print ('Reciclando cartón y papel por un año, puede tener una ganancia de', Ganancia_anual_Carton, 'pesos')
if menu == 3:
    print ('En su localidad se generan', Plasticos,'Kg de plásticos diarios')
    Ganancia_anual_plastico = Plasticos * Precio_Plastico_04_22 * 365
    print ('Reciclando los metales por un año, puede tener una ganancia de', Ganancia_anual_plastico, 'pesos')
if menu == 4: 
    print ('En su localidad se generan', Vidrios,'Kg de vidrio diarios')
    Ganancia_anual_vidrio = Vidrios * Precio_Vidrio_04_22 * 365
    print ('Reciclando los metales por un año, puede tener una ganancia de', Ganancia_anual_vidrio, 'pesos')  