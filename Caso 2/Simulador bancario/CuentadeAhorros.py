_author_= "Jesus David Pantoja Gonzalez"
_license_="GPL"
_version_="1.0.0"
_email_="recetjesusdavid123@gmail.com"

class CuentadeAhorros:
    # Aqui inicia la declaracion de mi clase
    
    '''#-----------------------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------------------------#'''
    __saldo__ = 0
    __Interes__ = 0.0
    '''#-----------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------#'''
    
    __method__= "consignarSaldo"
    __parameter__= "nuevoValor"
    __returns__ = "Valor de la cuenta"
    __Description__ = "metodo que retorna el valor de la cuenta"
    
    def consignarSaldo(self, nuevoValor):
        # Aqui inicia el codigo
        self.__saldo__ = self.__saldo__ + nuevoValor
        
    '''#-------------------------------------------------------------------#'''
    __method__= "darSaldo"
    __parameter__= "ninguno"
    __returns__ = "saldo de la cuenta"
    __Description__ = "metodo que retorna el saldo de la cuenta del cliente"
        
    def darSaldo(self):
        # Aqui inicia el codigo
        return self.__saldo__
        
    '''#-------------------------------------------------------------------#'''
        
    __method__= "RetirarValor"
    __parameter__= "monto"
    __returns__ = "valor de la cuenta"
    __Description__ = "metodo que retorna el valor de la cuenta"
        
    def RetirarSaldo(self, monto):
        # Aqui inicia el codigo
        self.__saldo__ = self.__saldo__ - monto
        
    '''#-------------------------------------------------------------------#'''
        
    __method__= "DarInteresMensual"
    __parameter__= "Ninguno"
    __returns__ = "Interes Mensual de la cuenta"
    __Description__ = "metodo que retorna el interes de la cuenta"
        
    def DarInteresMensual(self):
        # Aqui inicia el codigo
        return self.__InteresMensual__
        
    '''#-------------------------------------------------------------------#'''
        
    __method__= "actualizarSaldoPorPasoMes"
    __parameter__= "ninguno"
    __returns__ = "saldo de la cuenta"
    __Description__ = "metodo que actualiza el saldo de la cuenta"
        
    def actualizarSaldoPorPasoMes(self): 
        # Aqui inicia el codigo
        return self.__saldo__
        
    '''#-------------------------------------------------------------------#'''