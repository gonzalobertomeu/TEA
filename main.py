import computervision as core                       #archivo -> computervision.py
import analisis as math                             #archivo -> analisis.py

ret, video = core.capturarvideo()                   #captura video hasta presionar Q
if not ret:                                         #si ret es true, se capturo sin errores el video
    print("Error en la captura del video")
    exit()
video,vectoreventos = core.procesarvideo(video)     #dibuja puntos en video y guarda el vector de eventos
file = open("vectoreventos.txt","w")                #el vector de eventos se guarda en un archivo .txt
file.write(str(vectoreventos))
file.close()


vectorsonrisa = math.vector_sonrisa(vectoreventos)  #se procesa el vector sonrisa a partir del vector de eventos
vs = open("vector_sonrisa.txt","w")
vs.write(str(vectorsonrisa))
vs.close()

core.reproducirvideo(video)                         #se reproduce el video con los puntos dibujados

core.grabarvideo(video)                             #guarda el video en disco

math.graficar(vectorsonrisa)                        #muestra el grafico con las variaciones del modulo de vector sonrisa

