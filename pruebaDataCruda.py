import pandas as pd
import random as rd
import numpy as np

column_names = ["Accx","Accy","Accz","Apogeo1","Apogeo2","Tiempo",
             "Altura","Presion","GPSlat","GPSlong","Power","Fases","temp","girox","giroy","giroz"]

generador = np.zeros((1000,16))

for i in range(generador.shape[0]):
    for j in range(generador.shape[1]):
        if i == 0 or i== 1 or i== 2:
            generador[i][j] = round(rd.uniform(0,99), 4)    
        elif i== 3 or i==4:
            generador[i][j] = round(rd.uniform(0,1))  
        elif i== 5:
            generador[i][j] = round(rd.uniform(0,3000000))
        elif i== 6:
            generador[i][j] = round(rd.uniform(0,500000),2)
        elif i== 7:
            generador[i][j] = round(rd.uniform(0,1),9)
        elif i== 8 or i==9:
            generador[i][j] = round(rd.uniform(0,180),6)
        elif i== 10:
            generador[i][j] = round(rd.uniform(0,1))
        elif i== 11:
            generador[i][j] = round(rd.uniform(0,6))
        elif i== 12:
            generador[i][j] = round(rd.uniform(-40,90),3)
        elif i== 13:
            generador[i][j] = round(rd.uniform(0,180),6)
        elif i== 14 or i== 15 or i==16:
            generador[i][j] = round(rd.uniform(0,360),2)
        else:
            pass


##Imprimir el array de información
for i in range(generador.shape[0]):
    for j in range(generador.shape[1]):
        print(generador[i][j], end = " ")
    print("\n")

    