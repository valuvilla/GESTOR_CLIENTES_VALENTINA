from tkinter import *
from tkinter import ttk
from tkinter.messagebox import WARNING, askokcancel
from colorama import *
from termcolor import colored, cprint
import database as db
import helpers

class CenterWidgetMixin:
    def center(self,):
        self.update()
        w=self.winfo_width()
        h=self.winfo_height()
        ws=self.winfo_screenwidth()
        hs=self.winfo_screenheight()
        x=int((ws/2)-(w/2))
        y=int((hs/2)-(h/2))
        self.geometry('{}x{}+{}+{}'.format(w,h,x,y))

class MainWindows(Tk,CenterWidgetMixin):
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


        # Scrollbar
        barra_botones=Scrollbar(frame,orient=HORIZONTAL)
        barra_botones.pack(side=BOTTOM,fill=Y)

        treeview = ttk.Treeview(frame,yscrollcommand=barra_botones.set)
        treeview['columns']=('DNI','Nombre','Apellido')
        treeview.pack()


        # Completar treeview de clientes
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))



        treeview.pack()

        # Buttons frame
        frame_buttons=Frame(self)
        frame_buttons.pack(pady=20)

        #Buttons
        Button(frame_buttons,text=colored(Fore.GREEN+'Listar Clientes'),command=self.enumerate).grid(row=0,column=0,padx=10)
        Button(frame_buttons,text=colored(Fore.GREEN+'Crear Cliente'),command=self.create).grid(row=0,column=1,padx=10)
        Button(frame_buttons,text=colored(Fore.GREEN+'Editar Cliente'),command=self.edite).grid(row=0,column=2,padx=10)
        Button(frame_buttons,text=colored(Fore.RED+'Borrar Cliente'),command=self.delete).grid(row=0,column=3,padx=10)

        self.treeview=treeview

    def enumerate(self):
        self.treeview.delete(*self.treeview.get_children())
        for cliente in db.Clientes.lista:
            self.treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))

    def delete(self):
            cliente=self.treeview.focus()
            if cliente:
                campo=self.treeview.item(cliente, 'values')
                confirmar = askokcancel(
                    title=colored(Fore.GREEN+'Confirmar borrado'),
                    message=colored(Fore.RED+f'¿Estás seguro de que quieres borrar el cliente {campo[1]} {campo[2]}?', attrs=['bold']),
                    icon=WARNING
                )
                if confirmar:
                    self.treeview.delete(cliente)
                    db.Clientes.eliminar_cliente(campo[0]) #Borrar cliente de la base de datos


    def create(self):
        CreateClientWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)

            
class CreateClientWindow(Toplevel,CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(colored(Fore.GREEN+'Crear Cliente'))
        self.build()
        self.center()

        #Interactuar ventana
        self.transient()
        self.grab_set()        

    def build(self):
        frame=Frame(self)
        frame.pack(padx=20,pady=20)

        #Labels
        Label(frame,text=colored(Fore.BLUE+'DNI (2 int y 1 upper char):')).grid(row=0,column=0)
        Label(frame,text=colored(Fore.BLUE+'Nombre (2 a 30 chars):')).grid(row=0,column=1)
        Label(frame,text=colored(Fore.BLUE+'Apellido (2 a 30 chars):')).grid(row=0,column=2)

        #Entry
        dni=Entry(frame)
        dni.grid(row=1,column=0)
        dni.bind("<KeyRelease>", lambda ev: self.validate(ev,0))
        Nombre=Entry(frame)
        Nombre.grid(row=1,column=1)
        Nombre.bind("<KeyRelease>", lambda ev: self.validate(ev,1))
        Apellido=Entry(frame)
        Apellido.grid(row=1,column=2)
        Apellido.bind("<KeyRelease>", lambda ev: self.validate(ev,2))

        # Bottom frame
        frame=Frame(self)
        frame.pack(pady=10)

        # Buttons
        crear = Button(frame, text='Crear', command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text=colored(Fore.RED+'Cancelar'), command=self.close).grid(row=0, column=1)

        self.validaciones=[0,0,0]
        self.crear=crear
        self.dni=dni
        self.nombre=Nombre
        self.apellido=Apellido


    def create_client(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.agregar_cliente(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor= event.widget.get()
        valido = helpers.dni_valido(
            valor, db.Clientes.lista) if index == 0 else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure(bg='Green' if valido else 'Red')

        self.validaciones[index] = valido
        self.crear.configure(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(colored(Fore.GREEN+'Actualizar Cliente Cliente'))
        self.build()
        self.center()

        #Interactuar ventana
        self.transient()
        self.grab_set()

    def build(self):
        frame=Frame(self)
        frame.pack(padx=20,pady=10)

        #Labels
        Label(frame,text=colored(Fore.BLUE+'DNI (no editable):')).grid(row=0,column=0)
        Label(frame,text=colored(Fore.BLUE+'Nombre (2 a 30 chars):')).grid(row=0,column=1)
        Label(frame,text=colored(Fore.BLUE+'Apellido (2 a 30 chars):')).grid(row=0,column=2)

        #Entry
        dni=Entry(frame)
        dni.grid(row=1,column=0)
        dni.bind("<KeyRelease>", lambda ev: self.validate(ev,0))
        Nombre=Entry(frame)
        Nombre.grid(row=1,column=1)
        Nombre.bind("<KeyRelease>", lambda ev: self.validate(ev,1))
        Apellido=Entry(frame)
        Apellido.grid(row=1,column=2)
        Apellido.bind("<KeyRelease>", lambda ev: self.validate(ev,2))

        # Valores iniciales
        cliente=self.master.treeview.focus()
        campo=self.master.treeview.item(cliente, 'values')
        dni.insert(0,campo[0])
        dni.config(state=DISABLED)
        Nombre.insert(0,campo[1])
        Apellido.insert(0,campo[2])

        # Bottom frame
        frame=Frame(self)
        frame.pack(pady=10)

        # Buttons
        actualizar = Button(frame, text='Actualizar', command=self.update_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text=colored(Fore.RED+'Cancelar'), command=self.close).grid(row=0, column=1)

        # Actulizar botones activacion
        self.validaciones=[1,1]

        # Clases
        self.actualizar=actualizar
        self.dni=dni
        self.nombre=Nombre
        self.apellido=Apellido

    def validate(self, event, index):
        valor= event.widget.get()
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure(bg='Green' if valido else 'Red')

        self.validaciones[index] = valido
        self.actualizar.configure(state=NORMAL if self.validaciones == [1, 1] else DISABLED)

    def update_client(self):
        cliente=self.master.treeview.focus()
        self.master.treeview.item(cliente, values=(
            self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.modificar_cliente(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

