_author_= "Jesus David Pantoja Gonzalez"
_license_="GPL"
_version_="1.0.0"
_email_="recetjesusdavid123@gmail.com"

from Fecha import Fecha

class Empleado:
    # Aqui inicia la declaracion de mi clase
    
    '''#-----------------------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------------------------#'''
    
    nombre = ''
    apellido = ''
    salario = 0
    
    '''#-----------------------------------------------------------------------------------------
    # 1 = masculino, 2 = Femenino
    ---------------------------------------------------------------------------------------------#'''
    
    sexo = 0
    
    '''#-----------------------------------------------------------------------------------------
    # Asociar clases
    ---------------------------------------------------------------------------------------------#'''
    
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    '''#-----------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------#'''
    
    __method__= 'Cambiar Salario'
    __parameter__= "Nuevosalario"
    __returns__ = "el nuevo salario"
    __Description__ = "metodo que actualiza el salario del empleado"
    
    def CambiarSalario(self, Nuevosalario):
        # Aqui va mi codigo
        self.salario = Nuevosalario
    
    __method__= 'DarSalario'
    __parameter__= "Ninguno"
    __returns__ = "El Salario del Empleado"
    __Description__ = "metodo que retorna el Salario"    
    
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario
    
    __method__= 'DarNombre'
    __parameter__= "Ninguno"
    __returns__ = "El Nombre del empleado"
    __Description__ = "metodo que retorna el nombre digitado por el usuario"
    
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre
    
    __method__= 'DarFechadeIngreso'
    __parameter__= "Ninguno"
    __returns__ = "La fecha de ingreso"
    __Description__ = "metodo que retorna la fecha de ingreso del empleado"   
    
    def ConsultarFechaIngreso(self):
        # Aqui va mi codigo
        return self. fechaIngreso.Darfecha()
    
    __method__ = "calcularSalarioAnual"
    __parameter__= "Ninguno"
    __returns__ = "Salario anual"
    __Description__ = "Muestra el salario anual del empleado"
    
    def CalcularSalarioAnual(self):
        # Aqui va mi codigo
        # forma 1
        #total = self.salario*12
        #return total
        # Forma 2 
        return self.salario*12
    
    __method__ = "calcularImpuestoSalarioAnual"
    __parameter__= "Ninguno"
    __returns__ = "Impuesto del salario anual"
    __Description__ = "Muestra el impuesto del salario anual del empleado"
    
    def CalcularImpuestoSalarioAnual(self): 
        # Aqui va mi codigo
        # Forma 1
        #SalarioAnual = self.CalcularSalarioAnual();
        #ImpuestoAnual = SalarioAnual*0.19
        #return ImpuestoAnual
        # Forma 2
        return self.CalcularImpuestoSalarioAnual()*0.19
    
    __method__ = "calcularImpuestoSalarioMensual"
    __parameter__= "Ninguno"
    __returns__ = "Impuesto del salario mensual"
    __Description__ = "Muestra el impuesto del salario mensual del empleado"
    
    def CalcularImpuestoSalarioMensual(self):
        # Aqui va mi codigo
        return self.DarSalario()*0.19
