import serial
import matplotlib.pyplot as plt               # Librería que se encarga de dibujar
import matplotlib.animation as animation      # Librería que se encarga de animar las gráficas 
import threading                              # Modulo que permite hacer hilos separados   
import numpy as np 

gData = []                           # Se crea un array
gData.append([0.0])        # Se añade un array en cero "x"
gData.append([0.0])        # Se añade un array en uno "y"

def getData(out_Data):
    with serial.Serial("\\.\COM4", 9600) as ser:
        while True:
            line = ser.readline(). decode('utf-8')
            try:
                gData[1].append(float(line))    # Se cambia lo que se ha recibido por un flotante
                if len(out_Data[1]) > 500:      # limitar la cantidad de datos que se reciben
                    out_Data[1].pop(0)
            except:
                pass
            
dataCollector = threading.Thread(target = getData, args = (gData))       # Generar un proceso o hilo 
dataCollector.start()                                                    # se inicializa el hilo

# Animación
def update_line(num, hl, data):             # hl manejador de la linea
    dx = np.array(range(len(data[1])))      # Crear arrays 
    dy = np.array(data[1])
    hl.set_data(dx, dy)                     # setear nuevos datos
    return hl,

fig = plt.figure(figsize=(8, 6))            # Genera una figura y el tamaño de esta

# Cambiar la escala de la figura
plt.ylim(-100, 100)
plt.xlim(0, 500)

hl, = plt.plot(gData[0], gData[1])          # Dibujar una linea

line_ani = animation.FuncAnimation(fig, update_line, fargs = (hl, gData), interval = 50, blit = False)

plt.show()

dataCollector.join()                 # Espera al hilo 

"""
with serial.Serial("\\.\COM4", 9600) as ser:
    while True:
        line = ser.readline(). decode('utf-8')
        try:
            gData[1].append(float(line))    # Se cambia lo que se ha recibido por un flotante
            if len(gData[1]) > 5:           # limitar la cantidad de datos que se reciben
                gData[1].pop(0)
        except:
            pass
        print(gData[1])                     # Se muestran los datos de la "y "
""" 