_author_= "Jesus David Pantoja Gonzalez"
_license_="GPL"
_version_="1.0.0"
_email_="recetjesusdavid123@gmail.com"

class Fecha:
    # Aqui inicia la declaracion de mi clase
    
    '''#-----------------------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------------------------#'''
    
    dia = 0
    mes = 0
    anio = 0
    
    '''#-----------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------#'''
    # Este metodo retorna el dia
    __method__= 'DarDia'
    __parameter__= "Ninguno"
    __returns__ = "Dia"
    __Description__ = "metodo que retorna el dia"
    def Dardia(self):
        # Aqui va mi codigo
        return self.dia
        
    # Este metodo retorna el Mes
    __method__= 'DarMes'
    __parameter__= "Ninguno"
    __returns__ = "Mes"
    __Description__ = "metodo que retorna el Mes"
    def DarMes(Self):
        # Aqui va mi codigo
        return self.mes
    
    # Retorna el Año
    __method__= 'DarAnio'
    __parameter__= "Ninguno"
    __returns__ = "Anio"
    __Description__ = "metodo que retorna el año"
    def DarAnio(self):
        # Aqui va mi codigo
        return self.anio
    
    # Este metodo retorna la fecha
    
    __method__= 'DarFecha'
    __parameter__= "Ninguno"
    __returns__ = "La fecha de la clase"
    __Description__ = "metodo que retorna la fecha digitada por el usuario"
    
    def Darfecha(self):
        # Aqui va mi codigo
        return self.dia+'/'+self.mes+'/'+self.anio
        # Esto es igual a 0/0/0 pero si se le añade valores quedaria por ejemplo como 12/5/2024
    