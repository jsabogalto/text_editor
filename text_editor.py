from tkinter import *
from tkinter import filedialog
from io import open


ruta = "" #almacenar la ruta del fichero
def new():
    global ruta
    mensaje.set("New file")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("My editor")
    
    
def open_file():
    global ruta
    mensaje.set("Open file")
    ruta = filedialog.askopenfilename(
        initialdir='.', 
        filetype=(("Ficheros de texto", "*.txt"),), 
        title="Abrir un fichero de texto")
    
    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - My editor")

def save():
    mensaje.set("Save file")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado con exito.")
        
    else:
        save_as()
def save_as():
    global ruta
    mensaje.set("Save file as")
    fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("fichero guardado correctamente")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""
root = Tk()
root.title("My editor")

#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")

#Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

#monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")




root.config(menu=menubar)

root.mainloop()