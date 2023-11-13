simbolos = ['¿','?','.','.',';',':','¡','!']
numpalabras = 0
with open('citas.txt','r') as archivo:
    for linea in archivo:
        for simbolo in simbolos:
            linea = linea.replace(simbolo," ")
        palabras = linea.split()
        for palabra in palabras:
            numpalabras += 1
print("El texto contiene %s palabras" %numpalabras)