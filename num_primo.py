print("Este programa imprimira los numeros primos entre 0 y 250")


#creamos la funcion que evalúa si un número es primo y le pasamos como argumento el número a evaluar
def es_primo(num):
    for x in range (2,num): #creamos un ciclo que vaya del 2 al número a evaluar
        if (num%x) == 0: #si al aplicar la operación módulo al número a evaluar da como resultado 0 entonces no es un número primo, el número se divide hasta uno antes de el mismo
            return False
    return True #si al salir del ciclo no hubo una división con residuo de cero entonces si es un número primo
#recorremos los numeros a evaluar desde el 2 hasta el 250 (número - 1)
array = []
for numero in range (2, 251):
    if(es_primo(numero) == True): #si el retorno de la evaluación es verdadero entonces imprimimos el número
        array.append(numero) #guardamos en un arreglo el número primo
        #print(numero, "es primo")

print(array)
#print(es_primo(2))
#print(es_primo(8))
#print(es_primo(9))
#print(es_primo(11))

