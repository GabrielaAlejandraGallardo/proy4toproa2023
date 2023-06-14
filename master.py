from tkinter import *
from tkinter import ttk
from ventana import *
#En esta aplicación estamos inicializando nuestra primer ventana
def main():
    root=Tk()#Creamos el primer objeto tkinter
    root.wm_title("Crud tkinter y Mysql")#Titulo d ela ventana
    app=Ventana(root)#Creamos un objeto de tipo ventana
    app.mainloop()#le decimos que inicie la pagina
    
if __name__=="__main__":#el objeto main es para inicializar
   main()