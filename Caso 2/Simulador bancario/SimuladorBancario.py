_author_= "Jesus David Pantoja Gonzalez"
_license_="GPL"
_version_="1.0.0"
_email_="recetjesusdavid123@gmail.com"
from CuentaCorriente import CuentaCorriente
from CDT import CDT
from CuentadeAhorros import CuentadeAhorros


class SimuladorBancario:
    # Aqui inicia la declaracion de mi clase
    
    '''#-----------------------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------------------------#'''
    __Nombre__ = " "
    __Cedula__ = 0.0
    __MesActual__ = 0
    
    '''#-----------------------------------------------------------------------------------------
    # asociando las clases
    ---------------------------------------------------------------------------------------------#'''
    
    __CuentaCorriente__ = CuentaCorriente()
    __CDT__ = CDT()
    __CuentaAhorros__ = CuentadeAhorros()

    '''#-----------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------#'''
    __method__= 'DarNombre'
    __parameter__= "Ninguno"
    __returns__ = "El Nombre del Cliente"
    __Description__ = "metodo que retorna el nombre digitado por el usuario"
    def DarNombre(self):
        # Aqui inicia el codigo
        return self.Nombre
    '''#----------------------------------------------------------------------------------------#'''
    __method__= 'DarCedula'
    __parameter__= "Ninguno"
    __returns__ = "La Cedula del Cliente"
    __Description__ = "metodo que retorna la cedula digitado por el usuario"
    def DarCedula(self):
        # Aqui inicia el codigo
        return self.Cedula
    '''#----------------------------------------------------------------------------------------#'''
    __method__= 'DarSaldoTotal'
    __parameter__= "Ninguno"
    __returns__ = "El Saldo Total de la cuenta"
    __Description__ = "metodo que retorna el nombre digitado por el usuario"
    def DarSaldoTotal(self):
        # Aqui inicia el codigo
        return "tu saldo total de la cuenta Es " + self.CuentaAhorros.darSaldo()+self.CuentaCorriente.darSaldo()+self.CDT.darSaldo()
    
    
    __method__= 'DepositarCuentaCorriente'
    __parameter__= "Monto"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite deposistar en cuenta corriente"
    def DepositarCuentaCorriente(self,Monto):
        # Aqui inicia el codigo
        self.__CuentaCorriente__.consignarSaldo(Monto)
        
        
    __method__= 'CalcularSaldoTotal'
    __parameter__= "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        #total = self.__CuentaCorriente__.darSaldo()+self.__CuentaAhorros__.darSaldo()
        #return total
        # metodo 2
        return self.__CuentaCorriente__.darSaldo()+self.__CuentaAhorros__.darSaldo()
    
    __method__= 'PasarAhorroACorriente'
    __parameter__= "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo que permite calcular el saldo total de todas las cuentas"
    
    def PasarAhorroAcorriente(self):
        # Aqui va mi codigo
        saldoAhorros = self.__CuentaAhorros__.darSaldo()
        self.__CuentaAhorros__.RetirarSaldo(saldoAhorros)
        self.__CuentaCorriente__.consignarSaldo(saldoAhorros)
        
        #Ejemplo: si saldoAhorros es igual a 10000, en la segunda linea se quita los 10000 y en la tercera linea se le añade los 10000 a la cuenta corriente
        
    __method__= 'Ahorrar'
    __parameter__= "Monto"
    __returns__ = "Ninguna"
    __Description__ = "Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parámetro"
    
    def Ahorrar(self, Monto):
        # Aqui va mi codigo
        self.__CuentaCorriente__.RetirarSaldo(Monto)
        self.__CuentaAhorros__.consignarSaldo(Monto)
        
        
    __method__= 'RetirarAhorro'
    __parameter__= "Monto"
    __returns__ = "Ninguna"
    __Description__ = "Retira un valor dado de la cuenta de ahorros"
    
    def RetirarAhorro(self, Monto):
        #Aqui va mi codigo
        self.__CuentaAhorros__.RetirarSaldo(Monto)
        
    __method__= 'darSaldoCorriente'
    __parameter__= "Ninguno"
    __returns__ = "el saldo que hay en la cuenta corriente"
    __Description__ = "Retorna el saldo que hay en la cuenta corriente"
    
    def darSaldoCorriente(self):
        #Aqui va mi codigo
        return self.__CuentaCorriente__.darSaldo()
    
    __method__= 'retirarTodo'
    __parameter__= "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"
    
    def retirarTodo(self): 
        #Aqui va mi codigo
        SaldoCorriente = self.__CuentaCorriente__.darSaldo() 
        SaldoAhorro = self.__CuentaAhorros__.darSaldo()
        self.__CuentaCorriente__.RetirarSaldo(SaldoCorriente) 
        self.__CuentaAhorros__.RetirarSaldo(SaldoAhorro)
        
    
    __method__= 'DuplicarAhorro'
    __parameter__= "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Duplica la cantidad de dinero que hay en la cuenta de ahorros"
    
    def DuplicarAhorro(self):
        #Aquí va el codigo
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhoros.DarSaldo())