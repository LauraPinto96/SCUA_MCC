from matplotlib import pyplot as plt                                                                    # Librería para graficar
import numpy as np                                                                                      #

file = open('TRYFIN1.txt', 'r')                                                                           
table = [['Acc x', 'Acc y', 'Acc z', 'Apogeo', 'Apogeo 2', 'Tiempo', 'Apote 2', 'Apote 1', 'Altura']]   

for line in file.readlines():
    line = line.replace('{', '')
    line = line.replace('},', '')
    line = line.replace('Tiempo seg:  ,', 'Tiempo:')
    regs = line.split(',')
    vals = [float(i.split(':')[1].strip()) for i in regs]
    table.append(vals)
    #print(vals)
print(table)

from fastapi import FastAPI

app = FastAPI()

@app.get("/get-iris")
def get_iris():

    import pandas as pd
    iris = pd.read_csv(table)

    return iris