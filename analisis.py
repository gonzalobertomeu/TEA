import math                                 #libreria para matematicas
import matplotlib.pyplot as plt             # ...     para graficos
import numpy as np                          # ...     para matrices


def modulo_vector(ve,point):                         #recibe como parametro el vector de eventos   
    modulovector = []                          #inicializa el vector sonrisa
    p_x , p_y = point
    for evento in ve:                           #recorre el vector de eventos
        punto_uno = evento[p_x -1]              #define los puntos que se van a medir
        punto_dos = evento[p_y -1]
        x = punto_uno[0] - punto_dos[0] #diferencia del vector en X
        y = punto_uno[1] - punto_dos[1] #diferencia del vectoy en Y
        modulo = math.sqrt(pow(x,2)+pow(y,2))   #distancia entre puntos
        modulovector.append(modulo)            #lo pone en el vector sonrisa
    return modulovector


def graficar(vector,titulo):
    x = []                                      #define el eje X del grafico
    y = []                                      #define el eje Y del grafico
    for i, val in enumerate(vector):            #recorre los valores del vector
        x.append(i)                             #pone en X los indices de cada elemento del vector
        y.append(val)                           #pone en Y los valores de cada elemento del vector
    plt.plot(x,y, label="{}".format(titulo))     #comienza a dibujar
    plt.xlabel('Fotogramas')                        #Leyenda de X
    plt.ylabel('Modulos')                #Leyenda de Y
    plt.title('Vectores')                 #Titulo de la ventana
    plt.legend(loc="upper right")
    #plt.show()                                  #Muestra el grafico
    
    
def terminar_grafico():    
    plt.savefig("output/graficos/vector_global.png")
    plt.close()
        

























