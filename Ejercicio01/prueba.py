from Examen2 import examen
from random import *

print("Examen de programación\n")
nombre = input("Ingresa tu nombre: ")

incisos = ["a", "b", "c"]

for i, pregunta in enumerate(examen.getPreguntas(),1):
    print(f"\n{i}.", pregunta.getPregunta())
    options = pregunta.getOpciones().copy() #Copia de la lista de opciones por pregunta
    shuffle(options)
    #print(list(zip(incisos,options)))
    dic = dict(list(zip(incisos,options)))
    
    for inciso, option in dic.items():
        print("  ",f"{inciso})", option)
    
    answer = input("\n   Escribe el inciso de tu respuesta: ")
    while answer not in dic.keys():
        answer = input("   Opción inválida, escribe el inciso de tu respuesta: ")
    #print(dic[answer])
    pregunta.setRespuesta(dic[answer])

print(f"\n\nExamen de {nombre}")
print("Calificación: ", examen.calificar(),end = "\n\n")
print(examen.getCorrectas())
print(examen.getIncorrectas())



