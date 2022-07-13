import tkinter as tk                                        # Interface de python para Tcl/Tk
import matplotlib                                           # Librería para graficar

matplotlib.use('TkAgg')                                     # TkAgg backend, que está hecho para integrarse en Tkinter

from matplotlib.figure import Figure                        # Se importan las siguientes clases: Figure, FigureCanvasTkAggy, NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import (             # La clase Figure representa el área de dibujo en la que matplotlib se dibujarán los gráficos
    FigureCanvasTkAgg,                                      # La clase FigureCanvasTkAgg es una interfaz entre el Figure y Tkinter Canvas
    NavigationToolbar2Tk                                    # El NavigationToolbar2Tk es una barra de herramientas incorporada para la figura en el gráfico
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')

        # Tratamiento de datos
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # Crear una figura
        figure = Figure(figsize=(6, 4), dpi=100)          # El Figure objeto toma dos argumentos: tamaño en pulgadas y puntos por pulgada (ppp). En este ejemplo, crea una figura de 600×400 píxeles.

        # Crear objeto FigureCanvasTkAgg
        figure_canvas = FigureCanvasTkAgg(figure, self)   # Tenga en cuenta que el FigureCanvasTkAgg objeto no es un Canvas objeto sino que contiene un Canvas objeto

        # Crear barra de herramientas
        NavigationToolbar2Tk(figure_canvas, self)

        # Crear ejes
        axes = figure.add_subplot()

        # Crear el gráfico de barras
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # Finalmente, coloque el gráfico en la ventana raíz de Tkinter


if __name__ == '__main__':
    app = App()
    app.mainloop()