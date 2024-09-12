_author_= "Jesus David Pantoja Gonzalez"
_license_="GPL"
_version_="1.0.0"
_email_="recetjesusdavid123@gmail.com"

class CuentaCorriente:
    # Aqui inicia la declaracion de mi clase
    
    '''#-----------------------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------------------------#'''
    
    __saldo__ = 0
    
    '''#-----------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------#'''
    
    __method__= "consignarSaldo"
    __parameter__= "Monto"
    __returns__ = "Valor de la cuenta"
    __Description__ = "metodo que retorna el valor de la cuenta"
    
    def consignarSaldo(self, Monto):
        # Aqui inicia el codigo
        self.__saldo__ = self.__saldo__ + Monto
        
    '''#-------------------------------------------------------------------#'''
        
    __method__= "darSaldo"
    __parameter__= "ninguno"
    __returns__ = "saldo de la cuenta"
    __Description__ = "metodo que retorna el saldo de la cuenta del cliente"
        
    def darSaldo(self):
        # Aqui inicia el codigo
        return self.__saldo__
        
    '''#-------------------------------------------------------------------#'''
        
    __method__= "RetirarSaldo"
    __parameter__= "monto"
    __returns__ = "valor de la cuenta"
    __Description__ = "metodo que retorna el valor de la cuenta"
        
    def RetirarSaldo(self, monto):
        # Aqui inicia el codigo
        self.__saldo__ = self.__saldo__ - monto
        
    '''#-------------------------------------------------------------------#'''
