import pandas as pd
import random as rd
import numpy as np
from decimal import *
from IPython.display import display

column_names = ["EMPUJE","TEMP1","TEMP2","TEMP3"]

#generador = np.zeros((1000,25))

EMPUJE = []
TEMP1 = []
TEMP2 = []
TEMP3 = []

i = 0

while(i < 600): 
    #"EMPUJE"
    EMPUJE.append(round(rd.uniform(0,99), 4))    
    #"TEMP1","TEMP2","TEMP3"
    TEMP1.append(round(rd.uniform(-40,30),3))
    TEMP2.append(round(rd.uniform(-40,30),3))
    TEMP3.append(round(rd.uniform(-40,30),3))
    i += 1
    

df = pd.DataFrame(list(zip(EMPUJE, TEMP1, TEMP2, TEMP3)), \
    columns = column_names)

#display(df.to_string())
#print(df)

#Export pandas dataframe to a .csv file
df.to_csv('./CreatedData/BankTestingCrudaData.csv',sep='\t')