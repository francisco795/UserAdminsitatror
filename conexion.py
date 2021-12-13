import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='tu_base', 
                                            user = 'root',
                                            password ='')



    def inserta_usuario(self,id,nombre, correo, area, userred,idanydesk):
        cur = self.conexion.cursor()
        sql='''INSERT INTO users (ID, NOMBRE, CORREO, AREA, USERRED, IDANYDESK) 
        VALUES(NULL,'{}', '{}','{}', '{}','{}')'''.format(id, nombre, correo, area, userred, idanydesk)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_usuario(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM users " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_usuario(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM users WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_usuario(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM users WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  