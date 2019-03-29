import math                                 #libreria para matematicas
import matplotlib.pyplot as plt             # ...     para graficos
import numpy as np                          # ...     para matrices



### ESTA FUNCION vector_sonrisa() DEBE DE GENERALIZARSE ###
### PARA PODER PROCESAR CUALQUIER GESTUALIDAD DEFINIDA  ###
### CON DOS PUNTOS DE LA FORMA                          ###
def vector_sonrisa(ve):                         #recibe como parametro el vector de eventos   
    vectorsonrisa = []                          #inicializa el vector sonrisa
    for evento in ve:                           #recorre el vector de eventos
        labiosuperior = evento[51]              #define los puntos que se van a medir
        labioinferior = evento[57]
        x = labiosuperior[0] - labioinferior[0] #diferencia del vector en X
        y = labiosuperior[1] - labioinferior[1] #diferencia del vectoy en Y
        modulo = math.sqrt(pow(x,2)+pow(y,2))   #distancia entre puntos
        vectorsonrisa.append(modulo)            #lo pone en el vector sonrisa
    return vectorsonrisa

def graficar(vector):
    x = []                                      #define el eje X del grafico
    y = []                                      #define el eje Y del grafico
    for i, val in enumerate(vector):            #recorre los valores del vector
        x.append(i)                             #pone en X los indices de cada elemento del vector
        y.append(val)                           #pone en Y los valores de cada elemento del vector
    plt.plot(x,y)                               #comienza a dibujar
    plt.xlabel('Frames')                        #Leyenda de X
    plt.ylabel('Modulo Sonrisa')                #Leyenda de Y
    plt.title('Vector Sonrisa')                 #Titulo de la ventana
    plt.show()                                  #Muestra el grafico
