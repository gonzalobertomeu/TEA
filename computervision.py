import cv2
import dlib
import numpy as np


def capturarvideo():
    video = []                          #variable que mantiene una lista de fogramas en RAM
    camara = cv2.VideoCapture(0)        #Abre Camara
    if not camara.isOpened():           #Se fija si pudo abrirse
        print("No se pudo abrir la camara")
        return False, None
    while True:                         #Ciclo infinito hasta tocar letra Q
        ret, frame = camara.read()      #Captura de fotograma
        if not ret:                     #ret es true si fue bien capturado el fotograma
            print("Error en el stream de la camara")
            return False, None
        video.append(frame)             #agrega fotograma al video
        cv2.imshow("Capturando",frame)  #muestra el fotograma
        if cv2.waitKey(1) == ord('q'):  #espera para salir por la tecla Q
            break
    camara.release()                    #libera la camara
    cv2.destroyAllWindows()             #cierra todas las ventanas
    return True, video                  #un retorno de 2 variables (completado, video)


def reproducirvideo(video):
    delay = int(1000/30)                #define cuanto va a esperar para mostrar siguiente imagen / FPS
    for image in video:                 #recorro el video
        cv2.imshow("Reproduciendo",image)
        cv2.waitKey(delay)

def grabarvideo(video):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')    #codecs de video para guardar el archivo
    out = cv2.VideoWriter('output/video/output.avi',fourcc,30,(640,480))     #se inicializa el escritor de video
    for image in video:                 #recorro el video
        out.write(image)                #guardo un fotograma en el archivo 'outpur.avi'
    out.release()                       #libero el escritor

def shape_to_event(shape):              #transforma lo obtenido del shape_predictor a Eventos
    event = []                          #vector de coordenadas -> Cada evento tiene 68 coordenadas (x,y)
    for i in range(0,68):               #lleno el evento con las coordenadas del shape
        coord = (shape.part(i).x,shape.part(i).y)
        event.append(coord)
    return event

def procesarvideo(video):               #funcionalidad principal del sistema
    detector = dlib.get_frontal_face_detector()     #inicializo detector de caras
    predictor = dlib.shape_predictor("./sp_68.dat") #inicializo el predictor de formas con el archivo preentrenado './sp_68.dat'

    vectoreventos = []                  #vector que contiene eventos / cada elemento corresponde a un fotograma             

    for index,image in enumerate(video):                    #recorro el video -> cada ciclo correponde a un fotograma
        print("WIP Frame {}".format(index))
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)       #paso el fotograma a blanco y negro
        gray = cv2.equalizeHist(gray)                       #normalizo el fotograma (mejor contraste y brillo)
        dets = detector(image,1)                            #detecto las caras dentro del fotograma
        for face in dets:                                   #recorro las caras de la imagen
            shape = predictor(image,face)                   #obtengo la forma de la cara (68 puntos)
            event = shape_to_event(shape)                   #paso de shape a evento (vector de coordenadas)
            vectoreventos.append(event)                     
            for point in event:                               #recorro la forma -> cada ciclo corresponde a un punto
                #print(point)                                  #muestro por consola las coordenadas de cada punto procesado
                cv2.circle(image,point,1,(0,255,255),-1)      #dibujo un circulo en la imagen, con las coordenadas del punto
    return video,vectoreventos                              #retorno el video nuevo con los puntos dibujados, y el vector de eventos para
                                                            #despues procesar los gestos