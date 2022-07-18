import pandas as pd
import random as rd
import numpy as np
from decimal import *
from IPython.display import display

column_names = ["Accx","Accy","Accz","Apogeo1","Apogeo2","Tiempo",
             "Altura","Presion","GPSlat","GPSlong","Power","Fases","temp","girox","giroy","giroz"]

#generador = np.zeros((1000,16))

Accx = [] 
Accy = [] 
Accz = [] 
Apogeo1 = []  
Apogeo2 = [] 
Tiempo = [] 
Altura = []  
Presion = [] 
GPSlat = [] 
GPSlong = []  
Power = []  
Fases = [] 
temp = [] 
girox = [] 
giroy = [] 
giroz = [] 



#getcontext().prec = 6
presionTmp = 101326
i = 0

while(presionTmp > 0): 
    #"Accx","Accy","Accz"
    Accx.append(round(rd.uniform(0,99), 4)) 
    Accy.append(round(rd.uniform(0,99), 4))
    Accz.append(round(rd.uniform(0,99), 4))    
    #"Apogeo1","Apogeo2"
    Apogeo1.append(round(rd.uniform(0,99),4))
    Apogeo2.append(round(rd.uniform(0,99),4))
    #"Tiempo"[Segundos]
    Tiempo.append(round(rd.uniform(0,1800)))
    #"Altura"
    Altura.append(round(rd.uniform(0,5000),2))
    #"Presion"
    Presion.append(presionTmp)
    #"GPSlat", "GPSlong"
    GPSlat.append(round(rd.uniform(-180,180),6))
    GPSlong.append(round(rd.uniform(-180,180),6))
    #"Power"
    Power.append(round(rd.uniform(0,1)))
    #"Fases"
    Fases.append(round(rd.uniform(0,6)))
    #"temp"[Celsius]
    temp.append(round(rd.uniform(-40,30),3))
    #"girox", "giroy", "giroz"
    girox.append(round(rd.uniform(0,360),2))
    giroy.append(round(rd.uniform(0,360),2))
    giroz.append(round(rd.uniform(0,360),2))
    presionTmp -= 133.322
    i += 1
    

df = pd.DataFrame(list(zip(Accx, Accy, Accz, Apogeo1, Apogeo2, \
    Tiempo, Altura, Presion, GPSlat, GPSlong, Power, Fases, \
    temp, girox, giroy, giroz)), \
    columns = column_names)

#display(df.to_string())
#print(df)

#Export pandas dataframe to a .csv file
df.to_csv('./CreatedData/CrudaData1.csv',sep='\t')
    