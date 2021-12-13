from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from conexion import*


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.notebook = ttk.Notebook(self)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='#7EB1FC')
        self.frame4.grid(column=0, row=2)

        self.id = StringVar()
        self.nombre = StringVar()
        self.correo = StringVar()
        self.area = StringVar()
        self.userred = StringVar()
        self.idanydesk = StringVar()
        self.buscar = StringVar()

        self.base_datos = Registro_datos()
        self.create_wietgs()
        
        
    def create_wietgs(self):
        
        Label(self.frame1, text = '\tF Q C O N T R O L  \t ',bg='#3853FF',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Agregar FQCitos/a',fg='white', bg ='#FF662C', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Nombre',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Correo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Area',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'UserRed', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'IDAnydesk', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        

        Entry(self.frame2,textvariable=self.nombre , font=('Arial Baltic',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.correo , font=('Arial Baltic',12)).grid(column=1,row=2, padx= 5)
        Entry(self.frame2,textvariable=self.area , font=('Arial Baltic sans',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.userred , font=('Arial Baltic',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.idanydesk , font=('Arial Baltic',12)).grid(column=1,row=5)
       
        Label(self.frame4, text = 'Opciones',fg='white', bg ='#7EB1FC', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial Baltic',10,'bold'), bg='#32B2FC').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.limpiar_datos, text='LIMPIAR ENTRADA', font=('Arial Baltic',10,'bold'), bg='#32B2FC').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial Baltic',10,'bold'), bg='#32B2FC').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial Baltic',8,'bold'), bg='#32B2FC').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.buscar , font=('Arial Baltic',18), width=10).grid(column=0,row=2, pady=2, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='MOSTRAR DATOS GUARDADOS', font=('Arial Baltic',10,'bold'), bg='#3CFF1F').grid(columnspan=3,column=0,row=3, pady=8)
        #Button(self.frame4,command = self.mostrar_info, text='ACERCA DE', font=('Arial Baltic',10,'bold'), bg='#3CFF1F').grid(columnspan=3,column=0,row=3, pady=8)


        self.tabla = ttk.Treeview(self.frame3, height=20)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Nombre', 'Correo', 'Area', 'UserRed','idanydesk')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Correo', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Area', minwidth=100, width=120 , anchor='center')
        self.tabla.column('UserRed', minwidth=100, width=105, anchor='center')
        self.tabla.column('idanydesk', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='ID', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Correo', text='Correo', anchor ='center')
        self.tabla.heading('Area', text='Area', anchor ='center')
        self.tabla.heading('UserRed', text='UserRed', anchor ='center')
        self.tabla.heading('idanydesk', text='IDanydesk', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='black')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
    
    '''
    def ajustes(self):
        self.paginas.select([self.frame4])
    '''    
    

    def agregar_datos(self):
        self.tabla.get_children()
        id = self.id.get()
        nombre = self.nombre.get()
        correo = self.correo.get()
        area = self.area.get()
        userred = self.userred.get()
        idanydesk = self.idanydesk.get()
        datos = (nombre, correo, area, userred, idanydesk)
        if nombre and correo and area and userred and idanydesk !='':        
            self.tabla.insert('',0, text = nombre, values=datos)
            self.base_datos.inserta_usuario(nombre, correo, area, userred, idanydesk)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.nombre.set('')
        self.correo.set('')
        self.area.set('')
        self.userred.set('')
        self.idanydesk.set('')

    def buscar_nombre(self):
        nombre_usuario = self.buscar.get()
        nombre_usuario = str("'" + nombre_usuario + "'")
        nombre_buscado = self.base_datos.busca_usuario(nombre_usuario)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for datos in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_usuario()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])


    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_usuario(nombre)


    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
   

def main():
    
    ventana = Tk()
    ventana.wm_title("FQControl! (Alpha)")
    ventana.config(bg='#7FB2FC')
    #ventana.geometry('900x500')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        
    