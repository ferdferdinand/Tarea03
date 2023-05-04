from random import sample

class Pregunta:

    #Método constructor, se ingresa la pregunta y las tres opciones (la primera es la correcta)
    def __init__(self, pregunta = 'pregunta', opc1 = 'opc 1', opc2 = 'opc 2', opc3 = 'opc 3'):
        self.__pregunta = pregunta
        self.__opciones = [opc1, opc2, opc3]
        self.__respuesta = ''

    def getPregunta(self):
        return self.__pregunta
    
    def getOpciones(self):
        return self.__opciones

    def setRespuesta(self,respuesta):
        self.__respuesta = respuesta

    def getValidar(self):
        return self.__respuesta == self.__opciones[0]


class Examen:

    #Método constructor
    def __init__(self):
        self.__BancoPreguntas = [] #Todas las preguntas que se agreguen
        self.__copy = [] #Una copia de todas las preguntas
        self.__preguntas = [] #Lista con las 10 preguntas que se hacen
        self.__correctas = []
        self.__incorrectas = []
        
    def agregarP(self, pregunta = Pregunta()):
        self.__BancoPreguntas.append(pregunta) #Agregamos preguntas al examen
        self.__copy = self.__BancoPreguntas #Copiamos la lista de preguntas para trabajar sobre esto

    def getPreguntas(self):
        n = 10
        self.__preguntas = sample(self.__copy,n) #n preguntas aleatorias
        
        #Quitamos las preguntas que ya se utilizaron
        for pregunta in self.__preguntas:
            self.__copy.remove(pregunta)

        return self.__preguntas

    def calificar(self):
        self.__correctas = [] #Preguntas correctas
        self.__incorrectas = [] #Preguntas incorrectas
        for pregunta in self.__preguntas:
            if pregunta.getValidar(): 
                self.__correctas.append("Pregunta " + str(self.__preguntas.index(pregunta)+1))
            else:
                self.__incorrectas.append("Pregunta " + str(self.__preguntas.index(pregunta)+1))
        return len(self.__correctas)

    def getCorrectas(self):
        cadena = 'Correctas: \n'
        for c in self.__correctas:
            cadena += "\t" + c + "\n"
        return cadena
    
    def getIncorrectas(self):
        cadena = 'Incorrectas: \n'
        for c in self.__incorrectas:
            cadena += "\t" + c + "\n"
        return cadena


    


