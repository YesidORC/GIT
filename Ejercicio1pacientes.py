class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__lista_pacientes = [ ] #lista porq se van a manejar muchos pacientes
        self.__numero_pacientes = len(self.__lista_pacientes) #siempre depende del tamaño de la lista y no se puede modificar
    
    def ingresarPaciente(self):
        #Solicitar datos:
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")
        