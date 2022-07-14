import pandas as pd
import random as rd
import numpy as np
from decimal import *

column_names = ["Accx","Accy","Accz","Apogeo1","Apogeo2","Tiempo",
             "Altura","Presion","GPSlat","GPSlong","Power","Fases","temp","girox","giroy","giroz"]

#generador = np.zeros((1000,16))

Accx = [0.0] *10
Accy = [0.0] *10 
Accz = [0.0] *10 
Apogeo1 = [0.0] * 10 
Apogeo2 = [0.0] * 10
Tiempo = [0.0] * 10 
Altura = [0.0] * 10 
Presion = [0.0] * 10
GPSlat = [0.0] * 10
GPSlong = [0.0] * 10  
Power = [0.0] * 10 
Fases = [0.0] *10
temp = [0.0] * 10
girox = [0.0] * 10
giroy = [0.0] * 10
giroz = [0.0] * 10



#getcontext().prec = 6
presionTmp = 101326

for i in range(1,10):
    #"Accx","Accy","Accz"
    Accx[i], Accy[i], Accz[i] = round(rd.uniform(0,99), 4)    
    #"Apogeo1","Apogeo2"
    Apogeo1[i], Apogeo2[i] = rd.uniform(0,1) 
    #"Tiempo"
    Tiempo[i] = round(rd.uniform(0,1800))
    #"Altura"
    Altura[i] = round(rd.uniform(0,5000),2)
    #"Presion"
    presionTmp -= 133.322
    Presion[i] = presionTmp 
    #"GPSlat", "GPSlong"
    GPSlat[i], GPSlong[i] = round(rd.uniform(0,180),6)
    #"Power"
    Power[i] = round(rd.uniform(0,1))
    #"Fases"
    Fases[i] = round(rd.uniform(0,6))
    #"temp"[Celsius]
    temp[i] = round(rd.uniform(-40,30),3)
    #"girox", "giroy", "giroz"
    girox[i], giroy[i], giroz[i] = round(rd.uniform(0,360),2)
    

df = pd.DataFrame(list(zip(Accx, Accy, Accz, Apogeo1, Apogeo2, \
    Tiempo, Altura, Presion, GPSlat, GPSlong, Power, Fases, \
    temp, girox, giroy, giroz)), \
    columns = column_names)

df

    