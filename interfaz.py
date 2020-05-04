from tkinter import *

raiz = Tk()
raiz.title ("Interfaz Gráfica")
width = 900
height = 600
raiz.resizable (0,0)
micanvas = Canvas (raiz, bg ="lightgreen", width = width, height = height)
micanvas.pack()
fondo = PhotoImage(file = 'fondo.png')
micanvas.create_image(450,300, anchor=CENTER, image=fondo)
micanvas.pack()
micanvas.create_text(width/2, 100, text = "CUIDA A TUS PLANTAS", anchor = CENTER, font = ("Arial Black", "38"), fill = "forest green")
reg = PhotoImage(file = 'regar.png')
regar = Button(raiz, image = reg, width = 140, height= 125,  command = lambda: img_r(), justify = "right")
micanvas.create_window(450, 220, window = regar, anchor = CENTER)
pla = PhotoImage(file = 'plaga.png')
plaga = Button(raiz, image = pla, width = 140, height= 125, command = lambda: img_p(),  justify = "right")
micanvas.create_window(200, 350, anchor = CENTER, window=plaga)
dr = PhotoImage(file = "dron.png")
dron = Button(raiz, image = dr, width = 140, height= 125, command = lambda: img_d(),  justify = "right")
micanvas.create_window(450, 500, window= dron, anchor = CENTER)
rob = PhotoImage(file = 'robot.png')
robot = Button(raiz, image = rob, width = 140, height= 125,  command = lambda: img_rob(), justify = "right")
micanvas.create_window(700, 350, anchor = CENTER, window = robot)
sal= Button(raiz, width = 7, height= 2, anchor = CENTER, text = "Salir", command = lambda: salir(), font = ("Arial", "15"), bg = "indian red")
micanvas.create_window(800, 540, window = sal, anchor = CENTER)

def salir():
    """ Cierra la pestaña.
        """
    raiz.quit()

def img_r():
    global fondo1
    micanvas.pack_forget()
    fondo1 = PhotoImage(file = 'riego.png')
    canvas = Canvas(raiz, bg ="lightgreen", width = width, height = height)
    canvas.create_image(450,300, anchor=CENTER, image=fondo1)
    canvas.pack()
    atras = Button(raiz, width = 7, height= 2, anchor = CENTER, text = "Atrás", command = lambda: atras1(canvas), font = ("Arial", "15"), bg = "indian red" )
    canvas.create_window(800, 540, window = atras, anchor = CENTER)

def atras1(canvas):
    global micanvas
    canvas.pack_forget()
    micanvas.pack()

def img_p():
    global fondo2
    micanvas.pack_forget()
    fondo2 = PhotoImage(file = 'control.png')
    canvas2 = Canvas(raiz, bg ="lightgreen", width = width, height = height)
    canvas2.create_image(450,300, anchor=CENTER, image=fondo2)
    canvas2.pack()
    atras = Button(raiz, width = 7, height= 2, anchor = CENTER, text = "Atrás", command = lambda: atras1(canvas2), font = ("Arial", "15"), bg = "indian red" )
    canvas2.create_window(800, 540, window = atras, anchor = CENTER)

def img_d():
    global fondo3
    micanvas.pack_forget()
    fondo3 = PhotoImage(file = 'distribucion.png')
    canvas3 = Canvas(raiz, bg ="lightgreen", width = width, height = height)
    canvas3.create_image(450,300, anchor=CENTER, image=fondo3)
    canvas3.pack()
    atras = Button(raiz, width = 7, height= 2, anchor = CENTER, text = "Atrás", command = lambda: atras1(canvas3), font = ("Arial", "15"), bg = "indian red" )
    canvas3.create_window(800, 540, window = atras, anchor = CENTER)

def img_rob():
    global fondo4
    micanvas.pack_forget()
    fondo4 = PhotoImage(file = 'recolecta.png')
    canvas4 = Canvas(raiz, bg ="lightgreen", width = width, height = height)
    canvas4.create_image(450,300, anchor=CENTER, image=fondo4)
    canvas4.pack()
    atras = Button(raiz, width = 7, height= 2, anchor = CENTER, text = "Atrás", command = lambda: atras1(canvas4), font = ("Arial", "15"), bg = "indian red" )
    canvas4.create_window(800, 540, window = atras, anchor = CENTER)


raiz.mainloop()
