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
    #Inicializar
    def __init__(self):
        self.__lista_pacientes = [ ] #lista porq se van a manejar muchos pacientes
        self.__numero_pacientes = len(self.__lista_pacientes) #siempre depende del tamaño de la lista y no se puede modificar
    
    #Función ingresar paciente
    def ingresarPaciente(self):

        #Solicitar datos:
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")

        #Crear objeto y asignarle datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        #Guardar el paciente en la lista
        self.__lista_pacientes.append(p)

        #Actualizar la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    #Función ver # de pacientes
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    #Función ver datos de los pacientes
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: ")) #Asi lo identifica
        for paciente in self.__lista_pacientes: #Se busca paciente no cedula porq en la lista hay PACIENTES
            if cedula == paciente.verCedula(): #Si coincide cedula con paciente se muestran los datos:
                print ("Nombre: " + paciente.verNombre())
                print ("Cédula: " + str(paciente.verCedula()))
                print ("Género: " + paciente.verGenero())
                print ("Servicio: " + paciente.verServicio())

#Con los objetos de las clases se peude accedder a funciones o métodos
mi_sistema = Sistema() #Se crea una instancia de Sistema

while True: #Ciclo infinito

    #Crear menú
    opcion = int(input("1. Nuevo paciente - 2. Numero de pacientes - 3, Datos paciente - 4. Salir"))

    if opcion == 1: #Nuevo paciente
        mi_sistema.ingresarPaciente()
    elif opcion == 2: #Numero de pacientes
        print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3: #Datos paciente
        mi_sistema.verDatosPaciente()
    elif opcion == 4: #Salir
        break
    else: #Se equivocó (respuesta no válida)
        print("Opción no válida")
