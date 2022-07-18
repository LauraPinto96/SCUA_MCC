import pandas as pd
import random as rd
import numpy as np
from decimal import *
from IPython.display import display

column_names = ["GPSLAT","GPSLON","GPSALT","GPSSPE","HUM","TEMP","PRES","CO",
             "CO2","NH2","NH3","TVOC","COMX","COMY","COMZ","ACCX","ACCY",
             "ACCZ","GYRX","GYRY","GYRZ","BAT","VEL","ANGA","ANGB"]

#generador = np.zeros((1000,25))

GPSLAT = []
GPSLON = []
GPSALT = []
GPSSPE = []
HUM = []
TEMP =[]
PRES = []
CO = []
CO2 = []
NH2 = []
NH3 = []
TVOC = []
COMX = []
COMY = []
COMZ = []
ACCX = []
ACCY = []
ACCZ = []
GYRX = []
GYRY = []
GYRZ = []
BAT = []
VEL = []
ANGA = []
ANGB = []

#getcontext().prec = 6
presionTmp = 101326
i = 0

while(presionTmp > 0): 
    #"GPSLAT","GPSLON","GPSALT","GPSSPE"
    GPSLAT.append(round(rd.uniform(0,99), 4)) 
    GPSLON.append(round(rd.uniform(0,99), 4))
    GPSALT.append(round(rd.uniform(0,99), 4)) 
    GPSSPE.append(round(rd.uniform(0,99), 4))    
    #"HUM"
    HUM.append(round(rd.uniform(0,99),4))
    #"TEMP"
    TEMP.append(round(rd.uniform(-40,30),4))
    #"PRES"
    PRES.append(presionTmp)
    #"CO"
    CO.append(round(rd.uniform(0,99),4))
    #"CO2"
    CO2.append(round(rd.uniform(0,99),4))
    #"NH2"
    NH2.append(round(rd.uniform(0,99),4))
    #"NH3"
    NH3.append(round(rd.uniform(0,99),4))
    #"TVOC"
    TVOC.append(round(rd.uniform(0,99),4))
    #"COMX","COMY","COMZ"
    COMX.append(round(rd.uniform(0,360),2))
    COMY.append(round(rd.uniform(0,360),2))
    COMZ.append(round(rd.uniform(0,360),2))
    #"ACCX","ACCY","ACCZ"
    ACCX.append(round(rd.uniform(0,99), 4)) 
    ACCY.append(round(rd.uniform(0,99), 4))
    ACCZ.append(round(rd.uniform(0,99), 4)) 
    #"GYRX","GYRY","GYRZ"
    GYRX.append(round(rd.uniform(0,360),2))
    GYRY.append(round(rd.uniform(0,360),2))
    GYRZ.append(round(rd.uniform(0,360),2)) 
    #"BAT"
    BAT.append(round(rd.uniform(0,1)))
    #"VEL"
    VEL.append(round(rd.uniform(0,1800)))
    #"ANGA","ANGB"
    ANGA.append(round(rd.uniform(-180,180),6))
    ANGB.append(round(rd.uniform(-180,180),6))
    presionTmp -= 133.322
    i += 1
    

df = pd.DataFrame(list(zip(GPSLAT, GPSLON, GPSALT, GPSSPE, \
    HUM, TEMP, PRES, CO, CO2, NH2, NH3, TVOC, COMX, COMY, COMZ, \
    ACCX, ACCY, ACCZ, GYRX, GYRY, GYRZ, BAT, VEL, ANGA, ANGB)), \
    columns = column_names)

#display(df.to_string())
#print(df)

#Export pandas dataframe to a .csv file
df.to_csv('./CreatedData/CrudaDataCansat.csv',sep='\t')