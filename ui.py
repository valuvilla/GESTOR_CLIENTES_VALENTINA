from tkinter import *
from tkinter import ttk
from colorama import *
from termcolor import colored, cprint
import database as db


class CenterWingetMin:
    def center(self,):
        self.update()
        w=self.winfo_width()
        h=self.winfo_height()
        ws=self.winfo_screenwidth()
        hs=self.winfo_screenheight()
        x=int((ws/2)-(w/2))
        y=int((hs/2)-(h/2))
        self.geometry('{}x{}+{}+{}'.format(w,h,x,y))

class MainWindows(Tk,CenterWingetMin):
    def __init__(self):
        super().__init__()
        self.title(colored("Gestor de Clientes", 'white', attrs=['bold'], on_color='on_green'))
        self.build()
        self.center()

    def build(self):
        frame=Frame(self)
        frame.pack()

        #Treeview
        treeview= ttk.Treeview(frame)
        treeview['columns']=('DNI','Nombre','Apellido')
        treeview.pack()

        #Column format
        treeview.columns('#0',width=0,stretch=NO)
        treeview.column('DNI',anchor=CENTER,width=100)
        treeview.column('Nombre',anchor=CENTER,width=100)
        treeview.column('Apellido',anchor=CENTER,width=100)

        #Headings
        treeview.heading('#0',text='',anchor=CENTER)
        treeview.heading('DNI',text=colored(Fore.GREEN+'DNI'),anchor=CENTER)
        treeview.heading('Nombre',text=colored(Fore.GREEN+'Nombre'),anchor=CENTER)
        treeview.heading('Apellido',text=colored(Fore.GREEN+'Apellido'),anchor=CENTER)

        #Data
        treeview.pack()

        #Buttons
        barra_botones=Scrollbar(frame,orient=HORIZONTAL)
        barra_botones.pack(side=BOTTOM,fill=Y)

        treeview = ttk.Treeview(frame,yscrollcommand=barra_botones.set)
        treeview['columns']=('DNI','Nombre','Apellido')
        treeview.pack()


        # Completar treeview de clientes
        for cliente in db.Clientes.lista:
            treeview.insert('',0,text='',values=(cliente.dni,cliente.nombre,cliente.apellido))