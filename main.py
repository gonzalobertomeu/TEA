import computervision as core                       #archivo -> computervision.py
import analisis as math                             #archivo -> analisis.py
from diccionario import gestos as gestos             

ret, video = core.capturarvideo()                   #captura video hasta presionar Q
if not ret:                                         #si ret es true, se capturo sin errores el video
    print("Error en la captura del video")
    exit()
video,vectoreventos = core.procesarvideo(video)     #dibuja puntos en video y guarda el vector de eventos
file = open("output/vector/vectoreventos.txt","w")                #el vector de eventos se guarda en un archivo .txt
file.write(str(vectoreventos))
file.close()


for gesto, punto in gestos.items():
    vectorgesto = math.modulo_vector(vectoreventos,punto)
    gesto_file = open("output/vector/vector_{}.txt".format(gesto),"w")
    gesto_file.write(str(vectorgesto))
    gesto_file.close()
    math.graficar(vectorgesto,gesto)
math.terminar_grafico()

core.reproducirvideo(video)                         #se reproduce el video con los puntos dibujados

core.grabarvideo(video)                             #guarda el video en disco
