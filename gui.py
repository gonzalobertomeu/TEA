from tkinter import *
from tkinter import ttk

def saludar():
    print('BIENVENIDO')


master = Tk()
master.geometry('400x600')
master.configure(bg = 'blue')
master.title('Estoy Hueveando')
ttk.Button(master, text = 'SALIR', command=quit).pack(side= BOTTOM, anchor = E)
ttk.Button(master,text = 'ACCION',command = saludar).pack(side= BOTTOM, anchor = E)






master.mainloop()
