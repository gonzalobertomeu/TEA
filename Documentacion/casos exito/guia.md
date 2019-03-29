# Guía instalación Python / OpenCV / dlib

## Antes de comenzar

```bash
    sudo apt update
```
Para actualizar la lista de los repositorios remotos

---
## Python3

Para instalar Python 3 en Linux basados en Debian (Ubuntu / Mint / etc)
```bash
    sudo apt install python3
```
---

## PIP3 (pip de Python3)

```bash
    sudo apt install python3-pip
```
Para chequear la version de pip3 tipear

```bash
    pip3 --version
```
---

## OpenCV

Para instalar OpenCV para Python desde el gestor de paquetes pip3

```bash
   pip3 install opencv-python 
```

Se recomienda realizar este comando desde la carpeta donde esta ubicado el proyecto

```bash
   #Ejemplo
   cd /home/user/project 
```

Es también recomendable borrar versiones previas de OpenCV que no hayan sido instaladas desde pip3 para evitar conflictos.
**Opcional**

---

## dlib

Para instalar dlib para Python desde el gestor de paquetes pip3

```bash
   pip3 install dlib 
```
---

## Paquetes de PIP3

**pypi.org**

Es la página donde se listan los paquetes y librerías disponibles para instalar por pip3 y descargar.
Sería interesante buscar sobre librerías de implementación de GUI (interfaz grafica de usuario).

Tambien se encuentran librerías para mostrar gráficos, como 'matplotlib', una librería similar a la que utiliza MatLab para definir sus gráficos.
